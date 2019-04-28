import json

class BaseConfig(object):
    def save(self, file):
        with open(file, 'w') as f:
            json.dump(vars(self), f, sort_keys=True, indent=4)

    @classmethod
    def load(cls, file):
        with open(file) as f:
            variables = json.load(f)
            self = cls()
            for key, val in variables.items():
                setattr(self, key, val)
        return self

class ModelConfig(BaseConfig):
    """Wrapper class for model hyperparameters."""

    def __init__(self, char_emb_size=25, char_lstm_units=25, word_lstm_units=100, fc_units=100,
                 dropout=0.5):
        self.char_vocab_size = None
        self.char_embedding_size = char_emb_size
        self.char_lstm_units = char_lstm_units
        self.dropout = dropout
        self.word_lstm_units = word_lstm_units
        self.fc_units = fc_units

class TrainerConfig(object):
    """Wrapper class for training hyperparameters."""

    def __init__(self, batch_size=20, optimizer='adam', learning_rate=0.001, lr_decay=0.9,
                 clip_gradients=5.0, max_epoch=15, validation_split=0.2, early_stopping=True,
                 patience=3):

        # Batch size
        self.batch_size = batch_size

        # Optimizer for training the model.
        self.optimizer = optimizer

        # Learning rate for the initial phase of training.
        self.learning_rate = learning_rate
        self.lr_decay = lr_decay

        # If not None, clip gradients to this value.
        self.clip_gradients = clip_gradients

        # The number of max epoch size
        self.max_epoch = max_epoch

        # The ratio of validation data excluded from the whole training data
        self.validation_split = validation_split

        # Parameters for early stopping
        self.early_stopping = early_stopping
        self.patience = patience
