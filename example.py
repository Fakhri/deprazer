from deprazer.reader import read_corpus
from deprazer.wrappers import Deprazer

if __name__ == '__main__':
    corpus = read_corpus('train.csv')

    model = Deprazer()
    model.train(corpus)
    model.save('model')
    # model = Deprazer.load('model')
    # corpus = [element[0] for element in corpus]
    # corpus = ['so stressed']
    # result = model.predict_corpus(corpus)
    # print(result)
