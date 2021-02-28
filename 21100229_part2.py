'''
    Urdu text to Roman
'''

import sys

class Urdu2Roman:
    '''
        A class to convert Raw Input of Urdu Text to Roman
    '''
    def __init__(self):
        self.cons_IPAs = {
            "پ": "p",
            "ب": "b",
            "م": "m",
            "ت": "t̪",
            "ط": "t̪",
            "د": "d̪",
            "ٹ": "ʈ",
            "ڈ": "ɖ",
            "ن": "n",
            "ک": "k",
            "گ": "g",
            "ق": "q",
            "ع": "ʔ",
            "ف": "f",
            "و": "v",
            "س": "s",
            "ص": "s",
            "ث": "s",
            "ذ": "z",
            "ض": "z",
            "ظ": "z",
            "ز": "z",
            "ش": "ʃ",
            "ژ": "ʒ",
            "خ": "x",
            "غ": "ɣ",
            "ہ": "h",
            "ح": "h",
            "ل": "l",
            "ر": "r",
            "ڑ": "ɽ",
            "ی": "j",
            "چ": "ʧ",
            "ج": "ʤ"
        }
        self.cons_h_IPA = "ʰ"
        self.dictionary = {
            "پ": self.handle_cons_h,
            "ب": self.handle_cons_h,
            "م": self.handle_cons_h,
            "ت": self.handle_cons_h,
            "ط": self.handle_cons,
            "د": self.handle_cons_h,
            "ٹ": self.handle_cons_h,
            "ڈ": self.handle_cons_h,
            "ن": self.handle_noon,
            "ک": self.handle_cons_h,
            "گ": self.handle_cons_h,
            "ق": self.handle_cons,
            "ع": self.handle_cons,
            "ف": self.handle_cons,
            "و": self.handle_cons,
            "س": self.handle_cons,
            "ص": self.handle_cons,
            "ث": self.handle_cons,
            "ذ": self.handle_cons,
            "ض": self.handle_cons,
            "ظ": self.handle_cons,
            "ز": self.handle_cons,
            "ش": self.handle_cons,
            "ژ": self.handle_cons,
            "خ": self.handle_cons,
            "غ": self.handle_cons,
            "ہ": self.handle_cons,
            "ح": self.handle_cons,
            "ل": self.handle_cons_h,
            "ر": self.handle_cons_h,
            "ڑ": self.handle_cons_h,
            "چ": self.handle_cons_h,
            "ج": self.handle_cons_h,
            "و": self.handle_vao,
            "ں": self.handle_noon_ghunna,
            "ا": self.handle_alif,
            "آ": self.handle_alif_madaa,
            "ی": self.handle_choti_yay,
            "ے": self.handle_bari_yay,
            "ء": self.handle_hamza,
            "ھ": self.handle_haa,
            "ؤ": self.handle_vao_hamza
        }
        self.IPAs_Roman = {
            "p": "p",
            "d": "d",
            "b": "b",
            "m": "m",
            "t̪": "t",
            "d̪": "d",
            "t": "t",
            "ʈ": "t",
            "ɖ": "d",
            "n": "n",
            "g": "g",
            "q": "q",
            "ʔ": "e",
            "f": "f",
            "v": "v",
            "s": "s",
            "z": "z",
            "ʃ": "sh",
            "ʒ": "s",
            "x": "kh",
            "ɣ": "gh",
            "h": "h",
            "l": "l",
            "r": "r",
            "ɽ": "r",
            "j": "y",
            "ʧ": "ch",
            "ʤ": "jh",
            "ɑ:": "a",
            "ŋ": "n",
            "u": "u",
            "u:": "o",
            "ɔ": "ɔ",
            "ɔ:": "on",
            "o": "o",
            "o:": "o",
            "ɑ": "ɑ",
            "ɑ:": "a",
            "ə": "a",
            "ə:": "e",
            "ɑ̃:": "an",
            "i": "i",
            "i:": "i",
            "k": "k",
            "e:": "ey",
            "e": "e"
        }
    
    def handle_cons(self, word, pos):
        IPA = self.cons_IPAs[word[pos]]
        return IPA

    def handle_cons_h(self, word, pos):
        IPA = self.cons_IPAs[word[pos]]
        if (pos + 1) < len(word):
            if word[pos+1] == "ھ":
                IPA += self.cons_h_IPA
        return IPA

    def handle_noon(self, word, pos):
        IPA = "n"
        if (pos+1) < len(word) and word[pos+1] == "ھ":
            IPA += self.cons_h_IPA
        elif (pos-1) > 0 and (pos+1) < len(word):
            if word[pos-1] in self.cons_IPAs and word[pos+1] in self.cons_IPAs:
                IPA = "ŋ"
        return IPA

    def handle_vao(self, word, pos):
        IPA = "v"
        if pos == len(word)-1:
            IPA = "u:"
        elif (pos+1) < len(word):
            if word[pos+1] == "ا":
                IPA = "v"
            elif word[pos+1] == "ن":
                IPA = "ɔ:"
            elif (pos-1) > 0 and word[pos-1] == "ھ":
                IPA = "o:" 
            elif (pos-1) > 0 and word[pos-1] == "ا":
                IPA = ""
        return IPA

    def handle_noon_ghunna(self, word, pos):
        IPA = ""
        if (pos-1) >= 0 and (word[pos-1] == "آ" or word[pos-1] == "ا"):
            IPA = ""
        return IPA

    def handle_alif(self, word, pos):
        IPA = "ɑ:"
        if pos == 0 and word[pos+1] != "و":
            IPA = "ə"
        elif pos == 0 and word[pos+1] == "و":
            IPA = "ɔ:"
        elif pos != 0 and word[pos-1] in self.cons_IPAs:
            IPA = "ɑ:"
        elif pos+1 < len(word) and word[pos+1] == "ں":
            IPA = "ɑ̃:"
        return IPA

    def handle_alif_madaa(self, word, pos):
        IPA = "ɑ:"
        return IPA

    def handle_choti_yay(self, word, pos):
        IPA = "i:"
        if pos == len(word)-1:
            IPA = "i:"
        elif (pos-1) > 0 and word[pos-1] == "ھ":
            IPA = "e:"
        elif (pos+1) < len(word) and word[pos+1] == "ا":
            IPA = "j"
        return IPA

    def handle_bari_yay(self, word, pos):
        IPA = "e:"
        return IPA

    def handle_hamza(self, word, pos):
        IPA = "ə"
        return IPA

    def handle_haa(self, word, pos):
        IPA = ""
        if pos == len(word)-1:
            IPA = ""
        elif (pos+1) < len(word) and word[pos+1] in self.cons_IPAs:
            IPA = "ə"
        return IPA

    def handle_vao_hamza(self, word, pos):
        IPA = "o:"
        return IPA

    def normalize(self, word):
        normalized_word = None
        normalized_word = [letter for letter in word if letter in self.dictionary]
        return normalized_word

    def convert2IPA(self, word):
        IPA = ""
        normalized_word = self.normalize(word)
        for pos, letter in enumerate(normalized_word):
            IPA += self.dictionary.get(letter)(normalized_word, pos)
        return IPA

    def normaize_IPA(self, word):
        normalized_word = None
        normalized_word = [letter for letter in word if letter in self.IPAs_Roman or letter == ":" or letter == "ʰ"]
        return normalized_word

    def convert2Roman(self, word):
        Roman = []
        IPA = self.convert2IPA(word)
        normalized_IPA = self.normaize_IPA(IPA)
        pos, IPA_len = 0, len(normalized_IPA)
        while True:
            if pos == IPA_len:
                break
            if (pos+1) < IPA_len and normalized_IPA[pos+1] == ":":
                Roman.append(self.IPAs_Roman[normalized_IPA[pos]+normalized_IPA[pos+1]])
                pos += 1
            elif (pos+1) < IPA_len and normalized_IPA[pos+1] == "ʰ":
                Roman.append(self.IPAs_Roman[normalized_IPA[pos]]+"h")
                pos += 1
            else:
                Roman.append(self.IPAs_Roman[normalized_IPA[pos]])
            pos += 1
        Roman = " ".join(Roman)
        return Roman

def main():
    # Input words
    f = open(sys.argv[1], "r")
    words = f.readlines()

    convertor = Urdu2Roman() # Class object

    f = open("output_part2.txt", "w")
    for word in words:
        Roman = convertor.convert2Roman(word)
        f.write(Roman + "\n")

main()
