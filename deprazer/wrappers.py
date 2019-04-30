import os
import numpy as np

from .config import ModelConfig, TrainerConfig
from .preprocessor import Preprocessor
from .model import DepressionAnalyzer
from .trainer import Trainer

class Deprazer():
    model_file = 'model.h5'

    def __init__(self, char_emb_size=25, char_lstm_units=25, word_lstm_units=100, fc_units=100,
                 dropout=0.5, batch_size=32,
                 optimizer='adam', learning_rate=0.001, lr_decay=0.9, clip_gradients=5.0,
                 max_epoch=10, validation_split=0.1, early_stopping=True, patience=3):
        self.model_config = ModelConfig(char_emb_size, char_lstm_units, word_lstm_units, fc_units,
                                        dropout)

        self.trainer_config = TrainerConfig(batch_size, optimizer, learning_rate, lr_decay,
                                            clip_gradients, max_epoch, validation_split,
                                            early_stopping, patience)
        self.preprocessor = Preprocessor()
        self.model = None

    def train(self, corpus):
        clean_corpus = []
        for element in corpus:
            sentence = self.preprocessor.remove_mentions(element[0])
            sentence = self.preprocessor.remove_links(sentence)
            sentence = self.preprocessor.normalize_number(sentence)
            sentence = self.preprocessor.remove_nonpermitted_chars(sentence)
            if len(sentence) > 5:
                clean_corpus.append([sentence, element[1]])

        self.model_config.char_vocab_size = self.preprocessor.char_vocab_size
        self.model = DepressionAnalyzer()
        self.model.build(self.model_config)

        trainer = Trainer(self.model, self.trainer_config, preprocessor=self.preprocessor)
        trainer.train(np.asarray(clean_corpus))

    # def evaluate(self, corpus):
    #

    def save(self, dir_path):
        if not os.path.exists(dir_path):
            print('Making the model directory: {}'.format(dir_path))
            os.mkdir(dir_path)
        # self.preprocessor.save(os.path.join(dir_path, self.preprocessor_file))
        self.model.save(os.path.join(dir_path, self.model_file))

    @classmethod
    def load(cls, dir_path):
        if not os.path.exists(dir_path):
            raise OSError('Could not find the model directory.')
        else:
            self = cls()
            # self.preprocessor = Preprocessor.load(os.path.join(dir_path, cls.preprocessor_file))
            self.model = DepressionAnalyzer.load(os.path.join(dir_path, cls.model_file))

            return self
