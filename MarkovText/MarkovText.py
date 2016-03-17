from __future__ import division
from collections import defaultdict
import string
import re
import numpy as np

class CountProbPair:
    def __init__(self):
        self.count = 0
        self.prob = 0.0

class Markov:

    def __init__(self, n=2):
        #self.word_dict = defaultdict(lambda: defaultdict((int, float)))
        self.word_dict = defaultdict(lambda: defaultdict(CountProbPair))
        self.word_dict[('',)][''].prob = 0.0
        self.word_dict[('',)][''].count = 0
        self.n = n

    def add_to_dict(self, text):
        """ Generate word n-tuple and next word probability dict """
        n = self.n

        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s', text)
        # '' is a special symbol for the start of a sentence like pymarkovchain uses
        for sentence in sentences:
            sentence = sentence.replace('"','').replace('“','"').replace('”','"') # remove quotes
            words = sentence.strip().split()  # split each sentence into its constituent words
            if len(words) == 0:
                continue

            # first word follows a sentence end
            self.word_dict[("",)][words[0]].count += 1

            for j in range(1, n+1):
                for i in range(len(words) - 1):
                    if i + j >= len(words):
                        continue
                    word = tuple(words[i:i + j])
                    self.word_dict[word][words[i + j]].count += 1

                # last word precedes a sentence end
                self.word_dict[tuple(words[len(words) - j:len(words)])][""].count += 1

        # We've now got the db filled with parametrized word counts
        # We still need to normalize this to represent probabilities
        for word in self.word_dict:
            wordsum = 0
            for nextword in self.word_dict[word]:
                wordsum += self.word_dict[word][nextword].count
            if wordsum != 0:
                for nextword in self.word_dict[word]:
                    self.word_dict[word][nextword].prob = self.word_dict[word][nextword].count / wordsum

    def create_sentence(self, start=("",)):
        # next word
        sentence = list(start)
        nxt = self.next_word(start)
        while nxt:
            sentence.append(nxt)
            nxt = self.next_word(sentence[-self.n:])
        return ' '.join(sentence)

    def next_word(self, previous_words):
        """The next word that is generated by the Markov Chain
        depends on a tuple of the previous words from the Chain"""
        # The previous words may never have appeared in order in the corpus used to
        # generate the word_dict. Consequently, we want to try to find the previous 
        # words in orde, but if they are not there, then we remove the earliest word
        # one by one and recheck. This means that next word depends on the current state
        # but possible not on the entire state
        previous_words = tuple(previous_words)
        if previous_words != ("",): # the empty string 1-tuple (singleton tuple) is always there
            while previous_words not in self.word_dict:
                previous_words = tuple(previous_words[1:])
                if not previous_words:
                    return ""
        frequencies = self.word_dict[previous_words]
        inv = [(v.prob,k) for k, v in frequencies.items()]
        p, w = zip(*inv)
        return np.random.choice(w,1,p)[0]

    def create_sentences(self, num, start=("",)):
        par = ""
        for _ in range(num):
            par = par + self.create_sentence(start)
        return par


