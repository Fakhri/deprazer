import numpy as np
import csv

def read_corpus(path):
    corpus = []
    with open(path, encoding='ISO-8859-2') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            corpus.append([row[1].strip().lower(), int(row[2])])

    return corpus

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
