from collections import Counter
from nltk.tokenize import regexp_tokenize


class TextGenerator:

    def __init__(self, file):
        self.corpus = self.add_corpus(file)
        self.tokens = self.tokenize()
        self.bigrams = self.make_bigrams()
        self.head_dict = {}
        self.make_head_dict()

    @staticmethod
    def add_corpus(file):
        with open(file, 'r', encoding='utf-8') as f:
            return f.read()

    def tokenize(self):
        return regexp_tokenize(self.corpus, r'\S+')

    def make_bigrams(self):
        return [(self.tokens[ind-1], x) for ind, x in enumerate(self.tokens) if ind != 0]

    def make_head_dict(self):
        for head, tail in self.bigrams:
            self.head_dict.setdefault(head, Counter()).update([tail])

    def print_stats(self):
        print('Number of bigrams: ', len(self.bigrams), '\n')

    def get_bigram(self, index):
        try:
            bigram = self.bigrams[int(index)]
        except ValueError:
            return 'Value Error. Please input an integer.'
        except IndexError:
            return 'Index Error. Please input an integer that is in the range of the corpus.'
        return f'Head: {bigram[0]}\t\tTail: {bigram[1]}'

    def get_head(self, name):
        try:
            head = self.head_dict[name].most_common()
        except KeyError:
            tails = ['Key Error. The requested word is not in the model. Please input another word.']
        else:
            tab = max([len(x[0]) for x in head]) + 3
            tails = [f'Tail: {tail:<{tab}s}Count: {count}' for tail, count in head]
        return f'Head: {name}\n' + '\n'.join(tails)+'\n'


def main():
    tg = TextGenerator(input())
    cmd = input()
    while cmd != 'exit':
        print(tg.get_head(cmd))
        cmd = input()


if __name__ == '__main__':
    main()
