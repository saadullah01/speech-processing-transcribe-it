'''
    Urdu text to IPA

    Command Line Arguments:
    _______________________
    -----------------------

    - To calculate error:
    ---------------------
        python3 21100229_part1.py input.txt ground_truth.txt
    
    - To only get the output:
    -------------------------
        python3 21100229_part1.py input.txt
'''
import sys
from jiwer import wer

class Urdu2IPA:
    '''
        A class to convert Raw Input of Urdu Text to IPA letters
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
            "ه": "h",
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
            "ه": self.handle_cons,
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

    def convert(self, word):
        IPA = []
        normalized_word = self.normalize(word)
        for pos, letter in enumerate(normalized_word):
            IPA.append(self.dictionary.get(letter)(normalized_word, pos))
        IPA = " ".join(IPA)
        return IPA

def main():
    # Input words
    f = open(sys.argv[1], "r")
    words = f.readlines()
    ground_truth_IPAs, error_calc = None, False
    if len(sys.argv) > 2:
        error_calc = True
        # Output words
        f = open(sys.argv[2], "r")
        ground_truth_IPAs = f.readlines()

    convertor = Urdu2IPA() # Class object

    f = open("output_part1.txt", "w")
    outputs_IPA = []
    for i, word in enumerate(words):
        IPA = convertor.convert(word)
        outputs_IPA.append(IPA)
    f.writelines('\n'.join(outputs_IPA))
    f.write('\n')
    if error_calc:
        error = wer(outputs_IPA, ground_truth_IPAs)
        f.write(str("\nError = " + str(error) + "\n"))

main()
