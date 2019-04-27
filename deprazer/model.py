import numpy as np

from math import log
from tensorflow.keras.layers import Input, Embedding, Masking, Dropout, LSTM, TimeDistributed, Dense
from tensorflow.keras.layers.merge import Concatenate
from tensorflow.keras.models import Model

# class BaseModel(object):
#     def __init__(self):
#         self.model = None
#
#     def predict(self, features):
#         y_pred = self.model.predict(features, batch_size=1)
#         return y_pred

class Seq2SeqG2P():
    def __init__(self, config):
        inputs = Input(shape=(None,), dtype='int32')
        output = TimeDistributed(Dense(config.output_size, activation='softmax'))(output)

        self.model = Model(inputs=[inputs], outputs=[output])

        print('Model Summary')
        print(self.model.summary())

    def predict(self, features):
        y_pred = self.model.predict(features, batch_size=1)
        return y_pred

    def save(self, file_path):
        self.model.save_weights(file_path)

    def load(self, file_path):
        self.model.load_weights(file_path)

    def __getattr__(self, name):
        return getattr(self.model, name)
