import nltk
from collections import defaultdict, Counter


sample_text = """
hello how are you doing today i am doing well thank you what about you i am good as well thank you
"""

class NGramPredictor:
    def __init__(self, n=2):
        self.n = n
        self.ngrams = defaultdict(Counter)
        self.train(sample_text)

    def train(self, text):
        tokens = nltk.word_tokenize(text.lower())
        for i in range(len(tokens) - self.n + 1):
            context = tuple(tokens[i:i + self.n - 1])
            next_word = tokens[i + self.n - 1]
            self.ngrams[context][next_word] += 1

    def predict(self, context):
        context = tuple(context.lower().split()[-(self.n - 1):])
        if context in self.ngrams:
            return self.ngrams[context].most_common(1)[0][0]
        return "<next>"

predictor = NGramPredictor()

def predict_next(sentence):
    return predictor.predict(sentence)
