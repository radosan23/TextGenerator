from nltk.tokenize import regexp_tokenize


class TextGenerator:

    def __init__(self):
        self.corpus = None
        self.tokens = None

    def add_corpus(self, file):
        f = open(file, 'r', encoding='utf-8')
        self.corpus = f.read()
        f.close()

    def tokenize(self):
        self.tokens = regexp_tokenize(self.corpus, r'\S+')

    def print_stats(self):
        print('Corpus statistics')
        print('All tokens: ', len(self.tokens))
        print('Unique tokens: ', len(set(self.tokens)), '\n')

    def get_token(self, index):
        return self.tokens[index]


def main():
    tg = TextGenerator()
    tg.add_corpus(input())
    tg.tokenize()
    tg.print_stats()
    cmd = input()
    while cmd != 'exit':
        print(tg.get_token(int(cmd)))
        cmd = input()


if __name__ == '__main__':
    main()
