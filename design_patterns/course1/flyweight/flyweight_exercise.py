class Sentence:
    def __init__(self, plain_text):
        # todo
        self.words = plain_text.split(' ')
        self.formatting = []

    class WordItem:
        def __init__(self, index, capitalize=False):
            self.index = index
            self.capitalize = capitalize

    def __getitem__(self, item):
        word = self.WordItem(item)
        self.formatting.append(word)
        return word

    def __str__(self):
        result = []

        for i in range(len(self.words)):
            c = self.words[i]
            for r in self.formatting:
                if r.index == i and r.capitalize:
                    c = c.upper()
            result.append(c)
        return ' '.join(result)


if __name__ == '__main__':
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence)

    s = Sentence('alpha beta gamma')
    s[1].capitalize = True
    assert str(s), 'alpha BETA gamma'

