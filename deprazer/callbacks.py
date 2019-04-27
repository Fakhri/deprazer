import math
import numpy as np

from tensorflow.keras.callbacks import Callback, EarlyStopping

def get_callbacks(valid=(), log_result=False, early_stopping=True, patience=3):
    callbacks = []

    if early_stopping:
        callbacks.append(EarlyStopping(monitor='per', patience=patience, mode='min'))

    return callbacks
