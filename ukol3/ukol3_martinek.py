import argparse
from tokenize_words import Tokenize_words
from tokenize_words import create_bidict_for_alphabet
import time

"""Iterator for easy way to move in word for decryption."""
class PhaseIterator:

    def __init__(self, phase):
        self.phase = phase
        self.length = len(phase)
        self.position = 0

    """Return next letter for decrypt."""
    def next(self):
        letter = self.phase[self.position]
        self.position += 1
        if self.position == self.length:
            self.position = 0
        return letter

    """Jump to specific position."""
    def jump(self, length):
        self.position = (self.position + length) % self.length

    """Set to start."""
    def set_start(self):
        self.position = 0

"""Class for decrypt input text file, list of words, dictionary of language"""
class Decrypt:

    """Init all files and create dictionaries."""
    def __init__(self, text_file, word_passwords_file, output_file, words_check):
        try:
            self.text = open(text_file, "r")
        except:
            print("Text file not exist.")
            exit(1)
        try:
            self.words = open(word_passwords_file, "r")
        except:
            print("Words phase file not exist.")
            exit(1)
        
        if output_file != "-1":
            self.FLAG_out_file = True
            try:
                self.output_file = open(output_file, "w")
            except:
                print("Can`t create output file.")
                exit(1)
        else:
            self.FLAG_out_file = False
        self.dic_num = create_bidict_for_alphabet()
        self.word_list = {}
        with open(words_check, "r") as word_list:
            for word in word_list:
                self.word_list[word[:-1].lower()] = True

    def __del__(self):
        self.text.close()
        self.words.close()
        if self.FLAG_out_file:
            self.output_file.close()

    """Do decryption. Mastered. Check word with specific length and if only one phase good return."""
    def decrypt(self):
        word_length = 3
        try_words = 1
        text = Tokenize_words(self.text)
        while True:
            good_phase = {}
            for phase in self.words:
                if len(good_phase) >= 2:
                    break
                phase_it = PhaseIterator(phase[:-1].lower())
                text.set_start()
                for i in range(try_words):
                    posun, slovo = text.next_word(length=word_length)
                    phase_it.jump(posun)
                    dec = self.decrypt_one_word(slovo, phase_it)
                    if dec in self.word_list:
                        good_phase[phase[:-1].lower()] = True
                        break
            if len(good_phase) == 1:
                for i in good_phase:
                    print("DONE IT. Word is \"", i, "\"", sep = '')
                    self.decrypt_allit(i)
                    return True
            if len(good_phase) == 0:
                print("Never state :D")
                return False
            word_length += 1
            if word_length > 10:
                print("Bad road :D")
                return False
            self.words.seek(0)
        
    """Decrypt one word with password it iterator."""    
    def decrypt_one_word(self, word, phase_it):
        to_back = ""
        for i in word:
            to_back += self.dic_num[(self.dic_num.inv[i]-self.dic_num.inv[phase_it.next()])%26]
        return to_back

    """Decprypt all with get one password."""
    def decrypt_allit(self, phase):
        self.text.seek(0)
        tokens = Tokenize_words(self.text)
        phase_it = PhaseIterator(phase)
        while True:
            one = tokens.next_token()
            if isinstance(one, str):
                one = self.decrypt_one_word(one, phase_it)
            self.write_on(one)
            if tokens.get_position() == 0:
                break
        if not self.FLAG_out_file:
            print()

    """Print it to file if is specific or to terminal."""
    def write_on(self, message):
        if self.FLAG_out_file:
            self.output_file.write(str(message))
        else:
            print(message, sep='', end='')

cas = time.time()
parser=argparse.ArgumentParser("Encryptor for Viegeners cipher")
parser.add_argument("-t", help='File with text for decrypt.', required=True)
parser.add_argument("-w", help='File with words to decrypt.', required=True)
parser.add_argument("-c", help='File with check words for language to stop decrypting.', required=True)
parser.add_argument("-o", help='If defined decrypted text will be print to files', default="-1")
args = parser.parse_args()
decrypt = Decrypt(text_file=args.t, word_passwords_file=args.w, output_file=args.o, words_check=args.c)
if decrypt.decrypt():
    print("\nDecrypted in ", time.time()-cas, " sec.", sep='')