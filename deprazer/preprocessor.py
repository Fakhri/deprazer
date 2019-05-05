import os
import pickle
import numpy as np
import re

from pkg_resources import resource_filename
from urllib.parse import urlparse

class Preprocessor():

    PAD = '<PAD>'

    def __init__(self):
        self.vocab_char = {self.PAD: 0}
        with open(resource_filename(__name__, "resources/chars.txt")) as f:
            for line in f:
                self.vocab_char[line.strip()] = len(self.vocab_char)

    def transform(self, corpus, return_label=True):
        chars = []
        labels = []
        for element in corpus:
            char_ids = []
            for word in element[0].split():
                char_ids.append(self._get_char_ids(word))
            chars.append(char_ids)

            if return_label:
                labels.append(float(element[1]))

        sentences = self.pad_sequence(chars)

        return (sentences, labels) if return_label else sentences

    def remove_mentions(self, text):
        words = text.split()
        result = []
        for w in words:
            if not w.startswith('@'):
                result.append(w)
        return ' '.join(result)

    def remove_links(self, text):
        words = text.split()
        result = []
        for w in words:
            try:
                parts = urlparse(w)
                if parts[1] == '':
                    result.append(w)
            except:
                result.append(w)
        return ' '.join(result)

    def normalize_number(self, text):
        return re.sub(r'[0-9]', r'0', text)

    def remove_nonpermitted_chars(self, text):
        result = ''
        for c in text:
            if c in self.vocab_char or c == ' ':
                result += c
        return result

    def singularize_spaces(self, text):
        return ' '.join(text.split()).strip()

    def _get_char_ids(self, word):
        return [self.vocab_char[c] for c in word]

    def pad_sequence(self, char_ids, labels=None):
        char_ids = pad_sequences(char_ids, pad_tok=0, nlevels=2)
        return np.asarray(char_ids)

    @property
    def char_vocab_size(self):
        return len(self.vocab_char)

    def save(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, file_path):
        with open(file_path, 'rb') as f:
            p = pickle.load(f)
        return p

def _pad_sequences(sequences, pad_tok, max_length):
    """
    Args:
        sequences: a generator of list or tuple.
        pad_tok: the char to pad with.
    Returns:
        a list of list where each sublist has same length.
    """
    sequence_padded = []

    for seq in sequences:
        seq = list(seq)
        seq_ = seq[:max_length] + [pad_tok] * max(max_length - len(seq), 0)
        sequence_padded += [seq_]

    return sequence_padded

def pad_sequences(sequences, pad_tok, nlevels=1):
    """
    Args:
        sequences: a generator of list or tuple.
        pad_tok: the char to pad with.
    Returns:
        a list of list where each sublist has same length.
    """
    if nlevels == 1:
        max_length = len(max(sequences, key=len))
        sequence_padded = _pad_sequences(sequences, pad_tok, max_length)
    elif nlevels == 2:
        max_length_word = max(len(max(seq, key=len)) for seq in sequences)
        sequence_padded = []
        for seq in sequences:
            # all words are same length now
            sp = _pad_sequences(seq, pad_tok, max_length_word)
            sequence_padded += [sp]

        max_length_sentence = max([len(sequence) for sequence in sequences])
        sequence_padded = _pad_sequences(sequence_padded, [pad_tok] *
                                         max_length_word, max_length_sentence)
    else:
        raise ValueError('nlevels can take 1 or 2, not take {}.'.format(nlevels))

    return sequence_padded
