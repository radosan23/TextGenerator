from nltk.tokenize import regexp_tokenize


class TextGenerator:

    def __init__(self):
        self.corpus = None
        self.tokens = None
        self.bigrams = None

    def add_corpus(self, file):
        f = open(file, 'r', encoding='utf-8')
        self.corpus = f.read()
        f.close()

    def tokenize(self):
        self.tokens = regexp_tokenize(self.corpus, r'\S+')

    def make_bigrams(self):
        self.bigrams = [(self.tokens[x-1], self.tokens[x]) for x in range(len(self.tokens)) if x != 0]

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


def main():
    tg = TextGenerator()
    tg.add_corpus(input())
    tg.tokenize()
    tg.make_bigrams()
    tg.print_stats()
    cmd = input()
    while cmd != 'exit':
        print(tg.get_bigram(cmd))
        cmd = input()


if __name__ == '__main__':
    main()
