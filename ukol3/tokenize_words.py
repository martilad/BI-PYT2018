from bidict import bidict

"""Create bidirectional dictionary with alphabet to numbers."""
def create_bidict_for_alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    bialpha = bidict()
    for i, j in enumerate(alphabet):
        bialpha[i] = j
    return bialpha

"""Get input file to toneks words and other characters."""
class Tokenize_words:

    """Init load tokent in list. Can be buffered TO DO maybe :D."""
    def __init__(self, file):
        dic_num = create_bidict_for_alphabet()
        self.list_of_tokens = []
        word = ""
        for item in file:
            for i in item:
                if i.lower() in dic_num.inv:
                    word += i.lower()
                else:
                    if len(word) > 0:
                        self.list_of_tokens.append(word)
                    word = ""
                    self.list_of_tokens.append(OtherToken(i))
        if len(word) > 0:
            self.list_of_tokens.append(word)
        self.position = 0
        self.length = len(self.list_of_tokens)

    """Return nex word with specific length."""
    def next_word(self, length=0):
        jumped = 0
        for i in range(self.length):
            word = self.next_token()
            if isinstance(word, str):
                if len(word) >= length:
                    return jumped, word
                jumped += len(word)
        return None, None

    """Return next token in file."""
    def next_token(self):
        token = self.list_of_tokens[self.position]
        self.position += 1
        if self.position == self.length:
            self.position = 0
        return token

    """Return position in tokens."""
    def get_position(self):
        return self.position

    """Return number of tokens."""
    def get_len_list_tokens(self):
        return len(self.list_of_tokens)

    """Seek on strat in tokens."""
    def set_start(self):
        self.position = 0

"""Reprezent all special character tokens."""
class OtherToken:

    def __init__(self, token):
        self.token = token

    def __str__(self):
        return self.token

    def __len__(self):
        return len(self.token)

    """Return string token."""
    def get_token(self):
        return self.token
