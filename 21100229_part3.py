'''
    Roman to Urdu text
'''

import sys

class Roman2Urdu:
    '''
        A class to convert Input of Roman to Urdu Text
    '''
    def __init__(self):
        self.Roman_cons = {
            "p": "p",
            "t": "t",
            "k": "k",
            "b": "b",
            "d": "d",
            "g": "g",
            "m": "m",
            "n": "n",
            "f": "f",
            "v": "v",
            "s": "s",
            "sh": "ʃ",
            "z": "z",
            "zh": "ʒ",
            "q": "q",
            "ch": "ʧ",
            "j": "ʤ",
            "l": "l",
            "w": "w",
            "r": "r",
            "y": "j",
            "h": "h",
            "kh": "x",
            "gh": "ɣ",
            "ae": "ae"
        }
        self.cons_h_IPA = "ʰ"
        self.dictionary = {
            "p": self.handle_cons,
            "ph": self.handle_cons_h,
            "t": self.handle_cons,
            "th": self.handle_cons_h,
            "k": self.handle_cons,
            "b": self.handle_cons,
            "bh": self.handle_cons_h,
            "d": self.handle_cons,
            "dh": self.handle_cons_h,
            "g": self.handle_cons,
            "m": self.handle_cons,
            "mh": self.handle_cons_h,
            "n": self.handle_cons,
            "f": self.handle_cons,
            "v": self.handle_cons,
            "s": self.handle_cons,
            "sh": self.handle_cons,
            "z": self.handle_cons,
            "zh": self.handle_cons,
            "q": self.handle_cons,
            "ch": self.handle_cons,
            "j": self.handle_cons,
            "jh": self.handle_cons_h,
            "l": self.handle_cons,
            "lh": self.handle_cons_h,
            "w": self.handle_cons,
            "r": self.handle_cons,
            "h": self.handle_cons,
            "kh": self.handle_cons,
            "gh": self.handle_cons,
            "y": self.handle_cons,
            "a": self.handle_a,
            "o": self.handle_o,
            "iy": self.handle_iy,
            "ey": self.handle_ey,
            "aa": self.handle_aa,
            "i": self.handle_i,
            "h": self.handle_cons,
            "e": self.handle_e,
            "ae": self.handle_cons
        }
        self.IPA_Urdu = {
            "ə": "ا",
            "ʃ": "ش",
            "r": "ر",
            "f": "ف",
            "i:": "ی",
            "h": "ھ",
            "j": "ی",
            "a:": "ا",
            "n": "ن",
            "o": "و",
            "m": "م",
            "x": "خ",
            "t": "ت",
            "k": "ک",
            "l": "ل",
            "b": "ب",
            "s": "س",
            "e:": "ے",
            "ʤ": "ج",
            "q": "ق",
            "a": "آ",
            "ɣ": "غ",
            "p": "پ",
            "d": "د",
            "ʧ": "چ",
            "ɽ": "ڑ",
            "ʒ": "ژ",
            "ʔ": "ع",
            "g": "گ",
            "ae": "ی"
        }

    def handle_cons(self, word, pos):
        IPA = self.Roman_cons[word[pos]]
        return IPA

    def handle_cons_h(self, word, pos):
        IPA = self.Roman_cons[word[pos][0]]+self.cons_h_IPA
        return IPA

    def handle_a(self, word, pos):
        IPA = "a:"
        if pos == 0:
            IPA = "ə"
        return IPA

    def handle_o(self, word, pos):
        IPA = "o"
        if pos == 0:
            IPA = "v"
        return IPA

    def handle_iy(self, word, pos):
        IPA = "i:"
        return IPA

    def handle_ey(self, word, pos):
        IPA = "e:"
        return IPA

    def handle_aa(self, word, pos):
        IPA = "a"
        return IPA

    def handle_i(self, word, pos):
        IPA = "i:"
        if pos == 0:
            IPA = "a:"
        elif pos == len(word)-1:
            IPA = "i:"
        return IPA

    def handle_e(self, word, pos):
        IPA = ""
        if pos == 0:
            IPA = "i"
        return IPA

    def normalize(self, word):
        normalized_word = word[:-1].split(" ")
        return normalized_word

    def convert2IPA(self, word):
        IPA = []
        normalized_word = self.normalize(word)
        for pos, letter in enumerate(normalized_word):
            word_IPA = self.dictionary.get(letter)(normalized_word, pos)
            if word_IPA:
                IPA.append(word_IPA)
        return IPA
    
    def convert2Urdu(self, IPA):
        Urdu = []
        for _, letter in enumerate(IPA):
            Urdu.append(self.IPA_Urdu[letter])
        return Urdu

def main():
    # Input words
    f = open(sys.argv[1], "r")
    words = f.readlines()
    
    convertor = Roman2Urdu()
    f = open("output_part3.txt", "w")
    for word in words:
        IPA = convertor.convert2IPA(word)
        Urdu = ''.join(convertor.convert2Urdu(IPA))
        f.write(Urdu + "\n")

main()
