from collections import Counter
from nltk.tokenize import regexp_tokenize
from random import choices


class TextGenerator:

    def __init__(self, file):
        self.corpus = None
        self.tokens = None
        self.bigrams = None
        self.head_dict = {}
        self.preprocess(file)

    def preprocess(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            self.corpus = f.read()
        self.tokens = regexp_tokenize(self.corpus, r'\S+')
        self.bigrams = [(self.tokens[ind-1], x) for ind, x in enumerate(self.tokens) if ind != 0]
        for head, tail in self.bigrams:
            self.head_dict.setdefault(head, Counter()).update([tail])

    def show_tails(self, name):
        try:
            head = self.head_dict[name].most_common()
        except KeyError:
            tails = ['Key Error. The requested word is not in the model. Please input another word.']
        else:
            tab = max([len(x[0]) for x in head]) + 3
            tails = [f'Tail: {tail:<{tab}s}Count: {count}' for tail, count in head]
        return f'Head: {name}\n' + '\n'.join(tails)+'\n'

    def get_sentence(self):
        word = choices(list(self.head_dict.keys()))[0]
        sentence = [word, ]
        for _ in range(9):
            word = choices(*zip(*self.head_dict[word].items()))[0]
            sentence.append(word)
        return ' '.join(sentence)


def main():
    tg = TextGenerator(input())
    for _ in range(10):
        print(tg.get_sentence())


if __name__ == '__main__':
    main()
