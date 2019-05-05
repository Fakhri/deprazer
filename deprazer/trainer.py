import numpy as np

from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.callbacks import EarlyStopping

from .reader import generate_batch

class Trainer(object):

    def __init__(self, model, trainer_config, preprocessor=None):
        self.model = model
        self.trainer_config = trainer_config
        self.preprocessor = preprocessor

    def train(self, corpus):
        # Prepare training and validation data(steps, generator)
        num_train_data = len(corpus) - int(self.trainer_config.validation_split * len(corpus))

        indices = np.random.permutation(np.arange(len(corpus)))

        train_indices, val_indices, _ = np.split(indices, [num_train_data, len(corpus)])
        train_corpus = corpus[train_indices]
        val_corpus = corpus[val_indices]

        train_steps, train_batches = generate_batch(train_corpus, self.trainer_config.batch_size,
                                                    preprocessor=self.preprocessor)
        val_steps, val_batches = generate_batch(val_corpus, self.trainer_config.batch_size,
                                                preprocessor=self.preprocessor)

        if not self.model.is_compiled:
            optimizer = None
            if self.trainer_config.optimizer == 'adam':
                optimizer = Adam(lr=self.trainer_config.learning_rate,
                                 clipvalue=self.trainer_config.clip_gradients)
            elif self.trainer_config.optimizer == 'sgd':
                optimizer = SGD(lr=self.trainer_config.learning_rate,
                                clipvalue=self.trainer_config.clip_gradients)

            self.model.compile(loss='binary_crossentropy', metrics=['binary_accuracy'],
                               optimizer=optimizer)
            self.model.is_compiled = True

        # Prepare callbacks
        if self.trainer_config.early_stopping:
            callbacks = [EarlyStopping(monitor='val_binary_accuracy',
                                       patience=self.trainer_config.patience, mode='max')]

        # Train the model
        self.model.fit_generator(generator=train_batches, steps_per_epoch=train_steps,
                                 validation_data=val_batches, validation_steps=val_steps,
                                 verbose=1, epochs=self.trainer_config.max_epoch,
                                 callbacks=callbacks)
