import os
import pickle
import numpy as np
import csv

class Preprocessor():

    PAD = '<PAD>'

    def __init__(self):
        self.vocab_char = {}


def normalize_number(text):
    return re.sub(r'[0-9]', r'0', text)

def read_corpus(path):
    corpus = []
    with open(path, encoding='ISO-8859-2') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            corpus.append((row[1].strip(), row[2]))

    return np.asarray(corpus)

def generate_batch(corpus, batch_size, preprocessor=None):
    num_batches_per_epoch = int((len(corpus) - 1) / batch_size) + 1

    def data_generator():
        """
        Generates a batch iterator for a dataset.
        """
        data_size = len(corpus)

        while True:
            # Shuffle the data at each epoch
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_corpus = corpus[shuffle_indices]

            for batch_num in range(num_batches_per_epoch):
                start_index = batch_num * batch_size
                end_index = min((batch_num + 1) * batch_size, data_size)
                data = shuffled_corpus[start_index: end_index]
                if preprocessor:
                    yield preprocessor.transform(data)
                else:
                    yield ([sentence for sentence in data])

    return num_batches_per_epoch, data_generator()

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

def dense_to_one_hot(labels_dense, num_classes, nlevels=1):
    """Convert class labels from scalars to one-hot vectors."""
    if nlevels == 1:
        num_labels = labels_dense.shape[0]
        index_offset = np.arange(num_labels) * num_classes
        labels_one_hot = np.zeros((num_labels, num_classes), dtype=np.int32)
        labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
        return labels_one_hot
    elif nlevels == 2:
        # assume that labels_dense has same column length
        num_labels = labels_dense.shape[0]
        num_length = labels_dense.shape[1]
        labels_one_hot = np.zeros((num_labels, num_length, num_classes), dtype=np.int32)
        layer_idx = np.arange(num_labels).reshape(num_labels, 1)
        # this index selects each component separately
        component_idx = np.tile(np.arange(num_length), (num_labels, 1))
        # then we use `a` to select indices according to category label
        labels_one_hot[layer_idx, component_idx, labels_dense] = 1
        return labels_one_hot
    else:
        raise ValueError('nlevels can take 1 or 2, not take {}.'.format(nlevels))
