import os
import numpy as np

from .config import ModelConfig, TrainerConfig
from .preprocessor import Preprocessor, create_preprocessor
from .model import DepressionAnalyzer
from .trainer import Trainer

class Deprazer():
    config_file = 'config.json'
    weight_file = 'model_weights.h5'
    preprocessor_file = 'preprocessor.pkl'

    def __init__(self, dropout=0.1, batch_size=32,
                 optimizer='adam', learning_rate=0.001, lr_decay=0.9, clip_gradients=5.0,
                 max_epoch=10, validation_split=0.1, early_stopping=True, patience=3):
        self.model_config = ModelConfig()

        self.trainer_config = TrainerConfig(batch_size, optimizer, learning_rate, lr_decay,
                                            clip_gradients, max_epoch, validation_split,
                                            early_stopping, patience)
        self.model = None

    def train(self, corpus):


    # def evaluate(self, corpus):
    #

    def save(self, dir_path):
        if not os.path.exists(dir_path):
            print('Making the model directory: {}'.format(dir_path))
            os.mkdir(dir_path)
        self.preprocessor.save(os.path.join(dir_path, self.preprocessor_file))
        self.model_config.save(os.path.join(dir_path, self.config_file))
        self.model.save(os.path.join(dir_path, self.weight_file))

    @classmethod
    def load(cls, dir_path):
        if not os.path.exists(dir_path):
            raise OSError('Could not find the model directory.')
        else:
            self = cls()
            self.preprocessor = Preprocessor.load(os.path.join(dir_path, cls.preprocessor_file))
            self.model_config = ModelConfig.load(os.path.join(dir_path, cls.config_file))
            self.model = Deprazer(self.model_config)
            self.model.load(file_path=os.path.join(dir_path, cls.weight_file))

            return self
