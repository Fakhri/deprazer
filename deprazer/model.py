import os
import numpy as np

from tensorflow.keras.layers import Input, Embedding, Masking, Dropout, LSTM, TimeDistributed, \
                                    Bidirectional, Dense, Concatenate
from tensorflow.keras.models import Model, load_model

class DepressionAnalyzer(object):
    def __init__(self):
        self.model = None
        self.is_compiled = False

    def build(self, config):
        char_ids = Input(batch_shape=(None, None, None), dtype='int32', name='char_ids')
        char_emb = Embedding(input_dim=config.char_vocab_size,
                             output_dim=config.char_embedding_size,
                             mask_zero=True, name='char_embedding')(char_ids)
        char_emb = TimeDistributed(Bidirectional(LSTM(config.char_lstm_units)))(char_emb)

        if config.dropout > 0:
            char_emb = Dropout(config.dropout)(char_emb)
        layers = Bidirectional(LSTM(units=config.word_lstm_units))(char_emb)
        layers = Dense(config.fc_units, activation='tanh')(layers)
        output = Dense(1, activation='sigmoid')(layers)

        self.model = Model(inputs=[char_ids], outputs=[output])

        print(self.model.summary())

    # def predict(self, features):
    #     y_pred = self.model.predict(features, batch_size=1)
    #     return y_pred

    def save(self, file_path):
        self.model.save(file_path)

    @classmethod
    def load(cls, file_path):
        if not os.path.exists(file_path):
            raise OSError('Could not find the model file.')

        self = cls()
        self.model = load_model(file_path)
        self.is_compiled = self.model._is_compiled
        return self

    def __getattr__(self, name):
        return getattr(self.model, name)
