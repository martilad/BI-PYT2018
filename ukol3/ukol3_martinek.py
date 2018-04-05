import argparse
from tokenize_words import Tokenize_words
from tokenize_words import create_bidict_for_alphabet

from time import sleep



class PhaseIterator:
    def __init__(self, phase):
        self.phase = phase
        self.length = len(phase)
        self.position = 0
    def next(self):
        letter = self.phase[self.position]
        self.position += 1
        if self.position == self.length:
            self.position = 0
        return letter

    def jump(self, length):
        print(self.phase[self.position])
        self.position = (self.position + length) % self.length
        print(self.phase[self.position])

    def set_start(self):
        self.position = 0

class Decrypt:
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
            self.FLAG_out_file = true
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


    def decrypt(self):
        text = Tokenize_words(self.text)
        for i in range(2):
            jump, w = text.next_word(length = 4)
            print (">>", jump, "<<>>", w, "<<", sep='')
        for phase in self.words:
            phase_it = PhaseIterator(phase[:-1])
            phase_it.jump(10)
            print()
            



parser=argparse.ArgumentParser("Encryptor for Viegeners cipher")
parser.add_argument("-t", help='File with text for decrypt.', required=True)
parser.add_argument("-w", help='File with words to decrypt.', required=True)
parser.add_argument("-c", help='File with check words for language to stop decrypting.', required=True)
parser.add_argument("-o", help='If defined decrypted text will be print to files', default="-1")

args = parser.parse_args()
decrypt = Decrypt(text_file=args.t, word_passwords_file=args.w, output_file=args.o, words_check=args.c)
decrypt.decrypt()