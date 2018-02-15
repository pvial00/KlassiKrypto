import collections, random

class Affine:
    def __init__(self):
        self.alphabet = {}
        self.alphabet_rev = {}
        for x in range(0,26):
            self.alphabet[chr(x + 65)] = x
            self.alphabet_rev[x] = chr(x + 65)

    def encrypt(self, words):
        cipher_text = ""
        for letter in words:
            num = self.alphabet[letter]
            num = ((num * 5) + 8) % 26
            sub = self.alphabet_rev[num]
            cipher_text += sub
        return cipher_text

    def decrypt(self, words):
        plain_text = ""
        for letter in words:
            num = self.alphabet[letter]
            num = (21 * (num - 8)) % 26
            sub = self.alphabet_rev[num]
            plain_text += sub
        return plain_text

class Atbash:
    def __init__(self):
        self.alphabet = {}
        self.alphabet_rev = {}
        for y, x in enumerate(reversed(range(65,91))):
            self.alphabet[chr(y + 65)] = chr(x)
            self.alphabet_rev[chr(x)] = chr(y + 65)

    def encrypt(self, words):
        cipher_text = ""
        for letter in words:
            sub = self.alphabet[letter]
            cipher_text += sub
        return cipher_text

    def decrypt(self, words):
        plain_text = ""
        for letter in words:
            sub = self.alphabet_rev[letter]
            plain_text += sub
        return plain_text

class BaconBits:
    def __init__(self):
        self.alphabet = { 'A':'00000', 'B':'00001','C':'00010','D':'00011','E':'00100','F':'00101','G':'00110','H':'00111','I':'01000','J':'01000','K':'01001','L':'01010','M':'01011','N':'01100','O':'01101','P':'01110','Q':'01111','R':'10000','S':'10001','T':'10010','U':'10011','V':'10011','W':'10100','X':'10101','Y':'10110','Z':'10111' }
        self.alphabet_rev = { '00000':'A', '00001':'B','00010':'C','00011':'D','00100':'E','00101':'F','00110':'G','00111':'H','01000':'I','01000':'J','01001':'K','01010':'L','01011':'M','01100':'N','01101':'O','01110':'P','01111':'Q','10000':'R','10001':'S','10010':'T','10011':'U','10011':'V','10100':'W','10101':'X','10110':'Y','10111':'Z' }

    def encrypt(self, words):
        cipher_text = ""
        for letter in words:
            sub = self.alphabet[letter]
            cipher_text += sub + " "
        return cipher_text

    def decrypt(self, words):
        plain_text = ""
        for letter in words.split():
            sub = self.alphabet_rev[letter]
            plain_text += sub
        return plain_text

class Baconian:
    def __init__(self):
        self.alphabet = { 'A':'aaaaa', 'B':'aaaab','C':'aaaba','D':'aaabb','E':'aabaa','F':'aabab','G':'aabba','H':'aabbb','I':'abaaa','J':'abaaa','K':'abaab','L':'ababa','M':'ababb','N':'abbaa','O':'abbab','P':'abbba','Q':'abbbb','R':'baaaa','S':'baaab','T':'baaba','U':'baabb','V':'baabb','W':'babaa','X':'babab','Y':'babba','Z':'babbb' }
        self.alphabet_rev = { 'aaaaa':'A', 'aaaab':'B','aaaba':'C','aaabb':'D','aabaa':'E','aabab':'F','aabba':'G','aabbb':'H','abaaa':'I','abaaa':'J','abaab':'K','ababa':'L','ababb':'M','abbaa':'N','abbab':'O','abbba':'P','abbbb':'Q','baaaa':'R','baaab':'S','baaba':'T','baabb':'U','baabb':'V','babaa':'W','babab':'X','babba':'Y','babbb':'Z' }
    
    def encrypt(self, words):
        cipher_text = ""
        for letter in words:
            sub = self.alphabet[letter]
            cipher_text += sub + " "
        return cipher_text

    def decrypt(self, words):
        plain_text = ""
        for letter in words.split():
            sub = self.alphabet_rev[letter]
            plain_text += sub
        return plain_text

class Chaocipher:
    def __init__(self, left=[], right=[]):
        if len(left) == 0 and len(right) == 0:
            self.alpha_sub = ['H', 'X', 'U', 'C', 'Z', 'V', 'A', 'M', 'D', 'S', 'L', 'K', 'P', 'E', 'F', 'J', 'R', 'I', 'G', 'T', 'W', 'O', 'B', 'N', 'Y', 'Q']
	    self.alpha_master = ['P', 'T', 'L', 'N', 'B', 'Q', 'D', 'E', 'O', 'Y', 'S', 'F', 'A', 'V', 'Z', 'K', 'G', 'J', 'R', 'I', 'H', 'W', 'X', 'U', 'M', 'C']
        else:
            self.alpha_sub = left
            self.alpha_master = right
        self.left = self.alpha_sub
        self.right = self.alpha_master

    def permute_alpha_sub(self, letter):
        while True:
            step1 = self.alpha_sub.pop(0)
            if step1 == letter:
                self.alpha_sub.insert(0,step1)
                break
            else:
                self.alpha_sub.append(step1)
        step2 = self.alpha_sub.pop(1)
        self.alpha_sub.insert(12,step2)

    def permute_alpha_master(self, letter):
        while True:
            step1 = self.alpha_master.pop(0)
            if step1 == letter:
                self.alpha_master.insert(0,step1)
                break
            else:
                self.alpha_master.append(step1)
        step2 = self.alpha_master.pop(0)
        self.alpha_master.append(step2)
        step3 = self.alpha_master.pop(2)
        self.alpha_master.insert(12,step3)

    def encrypt(self, words):
        cipher_text = ""
        self.alpha_sub = list(self.left)
        self.alpha_master = list(self.right)
        for letter in words:
            pos = self.alpha_master.index(letter)
            sub = self.alpha_sub[pos]
            self.permute_alpha_sub(sub)
            self.permute_alpha_master(letter)
            cipher_text += sub
        return cipher_text

    def decrypt(self, words):
        plain_text = ""
        self.alpha_sub = list(self.left)
        self.alpha_master = list(self.right)
        for letter in words:
            pos = self.alpha_sub.index(letter)
            sub = self.alpha_master[pos]
            self.permute_alpha_sub(letter)
            self.permute_alpha_master(sub)
            plain_text += sub
        return plain_text

class Vigenere:
    def __init__(self, key):
        self.key = list(key)
        self.keylen = len(key)
        self.alphabets = {}
        self.alphabets_rev = {}
        for z, x in enumerate(range(65,91)):
                alphabet = collections.deque()
                alphabet_dict = {}
                alphabet_dict_rev = {}
                for y in range(65,91):
                        alphabet.append(chr(y))
                if z == 0:
                        shift_factor = z
                else:
                        shift_factor = z * -1
                alphabet.rotate(shift_factor)
                for y in range(65,91):
                        letter = alphabet.popleft()
                        alphabet_dict[chr(y)] = letter
                        alphabet_dict_rev[letter] = chr(y)
                self.alphabets[chr(x)] = alphabet_dict
                self.alphabets_rev[chr(x)] = alphabet_dict_rev

    def encrypt(self, secret):
        cipher_text = ""
        for x in range(0,len(secret)):
                keyi = self.key[ x % self.keylen]
                sub_dict = self.alphabets[keyi]
                sub = sub_dict[secret[x]]
                cipher_text += sub
        return cipher_text

    def decrypt(self, secret):
        plain_text = ""
        for x in range(0,len(secret)):
                keyi = self.key[ x % self.keylen]
                sub_dict = self.alphabets_rev[keyi]
                sub = sub_dict[secret[x]]
                plain_text += sub
        return plain_text

class Beale:
    def __init__(self, book):
        self.dictionary = self.create_dictionary(book)
        self.dictionary_rev = list(self.dictionary)
        
    def create_dictionary(self, book):
        try:
            book_fd = open(book, "r")
        except IOError as ier:
            print "Error: Unable to open book file"
            exit(1)
        text = book_fd.read()
        book_fd.close()
        master_list = []
        for index, word in enumerate(text.split()):
            if index == 0:
                index = 1
            master_list.append(word[0])
        return master_list

    def encrypt(self, words):
        cipher_text = ""
        for letter in words:
            if letter != ' ':
            	sub = self.dictionary.index(letter)
            	pop_sub = self.dictionary.pop(sub)
            	self.dictionary.append(pop_sub)
            	cipher_text += str(sub) + " "
        return cipher_text

    def decrypt(self, numbers):
        plain_text = ""
        for number in numbers.split():
            if number != " " and number != "":
                num = int(number)
                sub = self.dictionary_rev.pop(num)
                self.dictionary_rev.append(sub)
                plain_text += sub
        return plain_text

class BitChao:
    def __init__(self, left=None, right=None):
        if left == None and right == None:
            self.alpha_sub = [142, 71, 43, 156, 130, 37, 39, 126, 81, 18, 153, 233, 202, 154, 178, 160, 144, 78, 120, 10, 155, 49, 105, 176, 185, 67, 195, 7, 215, 75, 3, 47, 220, 219, 162, 13, 183, 208, 254, 182, 187, 86, 163, 243, 166, 168, 152, 249, 242, 107, 136, 48, 252, 179, 25, 170, 221, 16, 177, 98, 5, 53, 164, 203, 225, 250, 118, 180, 173, 211, 113, 169, 93, 104, 88, 29, 55, 236, 174, 84, 22, 217, 119, 161, 32, 60, 117, 73, 59, 194, 206, 85, 58, 241, 239, 232, 100, 94, 34, 62, 28, 192, 204, 17, 4, 45, 189, 186, 19, 141, 199, 6, 223, 127, 247, 237, 111, 132, 103, 129, 80, 38, 198, 227, 212, 46, 145, 197, 229, 8, 92, 36, 234, 231, 255, 124, 240, 172, 27, 251, 207, 30, 54, 213, 91, 188, 158, 61, 151, 125, 128, 87, 69, 238, 63, 196, 109, 1, 121, 210, 96, 171, 74, 102, 12, 146, 209, 131, 9, 224, 106, 245, 95, 216, 56, 122, 50, 228, 159, 222, 79, 65, 40, 108, 57, 190, 70, 23, 0, 244, 157, 165, 138, 110, 14, 11, 101, 68, 90, 137, 33, 140, 72, 114, 205, 193, 44, 135, 77, 184, 97, 230, 167, 123, 99, 148, 2, 51, 64, 200, 133, 139, 147, 175, 134, 115, 116, 21, 150, 24, 52, 35, 235, 191, 15, 149, 201, 253, 26, 31, 20, 248, 112, 181, 218, 226, 82, 214, 143, 89, 41, 83, 66, 76, 246, 42]
            self.alpha_master = [243, 114, 14, 189, 193, 94, 22, 211, 4, 117, 49, 34, 118, 58, 184, 106, 92, 131, 109, 134, 19, 175, 221, 3, 141, 239, 245, 67, 147, 186, 182, 132, 57, 104, 5, 10, 202, 191, 8, 158, 187, 238, 112, 121, 126, 201, 80, 1, 170, 113, 71, 155, 223, 128, 137, 148, 91, 190, 29, 222, 154, 44, 165, 251, 230, 63, 64, 146, 120, 203, 83, 17, 188, 59, 195, 217, 130, 198, 151, 207, 68, 53, 142, 133, 173, 99, 143, 46, 240, 123, 16, 45, 122, 163, 152, 196, 73, 139, 233, 145, 242, 52, 205, 54, 2, 12, 135, 209, 229, 125, 100, 168, 228, 48, 90, 172, 40, 250, 26, 110, 237, 140, 200, 225, 23, 107, 213, 105, 232, 185, 156, 247, 171, 87, 20, 235, 138, 33, 65, 180, 167, 24, 15, 169, 79, 96, 93, 30, 210, 136, 102, 162, 25, 164, 220, 246, 75, 32, 18, 116, 38, 78, 254, 56, 31, 215, 13, 253, 161, 248, 69, 39, 174, 227, 160, 197, 119, 89, 111, 177, 6, 55, 60, 21, 82, 36, 108, 208, 50, 249, 234, 28, 85, 115, 153, 129, 42, 103, 150, 74, 224, 41, 214, 84, 27, 159, 181, 178, 231, 199, 204, 72, 176, 86, 192, 212, 166, 76, 88, 194, 101, 255, 244, 206, 124, 62, 35, 183, 70, 95, 51, 149, 219, 218, 179, 43, 61, 66, 226, 47, 37, 241, 252, 144, 77, 9, 236, 98, 127, 157, 7, 11, 97, 0, 81, 216]
        else:
            self.alpha_sub = left
            self.alpha_master = right
        self.left = self.alpha_sub
        self.right = self.alpha_master

    def gen_alphabet(self):
        alphabet = []
        alphabet_rev = []
        for x in range(0,256):
            alphabet.append(x)
            alphabet_rev.append(x)
            random.shuffle(alphabet)
            random.shuffle(alphabet_rev)
        return alphabet, alphabet_rev

    def permute_alpha_sub(self, letter):
        index = self.alpha_sub.index(letter)
        step1 = self.alpha_sub.pop(0)
        self.alpha_sub.insert(index,step1)
        step2 = self.alpha_sub.pop(1)
        self.alpha_sub.insert(128,step2)

    def permute_alpha_master(self, letter):
        index = self.alpha_master.index(letter)
        step1 = self.alpha_master.pop(0)
        self.alpha_master.insert(index,step1)
        step2 = self.alpha_master.pop(0)
        self.alpha_master.append(step2)
        step3 = self.alpha_master.pop(2)
        self.alpha_master.insert(128,step3)

    def encrypt(self, words):
        cipher_text = ""
        self.alpha_sub = list(self.left)
        self.alpha_master = list(self.right)
        for letter in words:
            char = ord(letter)
            pos = self.alpha_master.index(char)
            sub = self.alpha_sub.pop(pos)
            self.alpha_sub.insert(pos,sub)
            self.permute_alpha_sub(sub)
            self.permute_alpha_master(char)
            cipher_text += chr(sub)
        return cipher_text

    def decrypt(self, words):
        plain_text = ""
        self.alpha_sub = list(self.left)
        self.alpha_master = list(self.right)
        for letter in words:
            char = ord(letter)
            pos = self.alpha_sub.index(char)
            sub = self.alpha_master.pop(pos)
            self.alpha_master.insert(pos,sub)
            self.permute_alpha_sub(char)
            self.permute_alpha_master(sub)
            plain_text += chr(sub)
        return plain_text

class Caesar:
    def __init__(self, rot=3, alphabet_start=32, alphabet_end=122):
        self.rot = rot
        self.alphabet_size = alphabet_end - alphabet_start
        self.alphabet = {}
        self.alphabet_rev = {}
        for c, x in enumerate(range(alphabet_start, alphabet_end+1)):
            self.alphabet[c] = chr(x)
            self.alphabet_rev[chr(x)] = c

    def encrypt(self, text):
        cipher_text = ""
        for char in text:
            sub = (self.alphabet_rev[char] + self.rot) % self.alphabet_size
            sub_chr = self.alphabet[sub]
            cipher_text += sub_chr
        return cipher_text

    def decrypt(self, text):
        plain_text = ""
        for char in text:
            sub = (self.alphabet_rev[char] - self.rot) % self.alphabet_size
            sub_chr = self.alphabet[sub]
            plain_text += sub_chr
        return plain_text

class BitVigenere:
    def __init__(self, key):
        self.key = list(key)
        self.keylen = len(key)
        self.alphabets = {}
        self.alphabets_rev = {}
        for z, x in enumerate(range(256)):
                alphabet = collections.deque()
                alphabet_dict = {}
                alphabet_dict_rev = {}
                for y in range(256):
                        alphabet.append(y)
                if z == 0:
                        shift_factor = z
                else:
                        shift_factor = z * -1
                alphabet.rotate(shift_factor)
                for y in range(256):
                        letter = alphabet.popleft()
                        alphabet_dict[y] = letter
                        alphabet_dict_rev[letter] = y
                self.alphabets[x] = alphabet_dict
                self.alphabets_rev[x] = alphabet_dict_rev

    def encrypt(self, secret):
        cipher_text = ""
        for x in range(0,len(secret)):
                keyi = self.key[ x % self.keylen]
                sub_dict = self.alphabets[ord(keyi)]
                sub = sub_dict[ord(secret[x])]
                cipher_text += chr(sub)
        return cipher_text

    def decrypt(self, secret):
        plain_text = ""
        for x in range(0,len(secret)):
                keyi = self.key[ x % self.keylen]
                sub_dict = self.alphabets_rev[ord(keyi)]
                sub = sub_dict[ord(secret[x])]
                plain_text += chr(sub)
        return plain_text

class Twist:
    def rev_words(self, words):
        newwords = []
        newstring = ""
        for letter in words:
            newwords.append(letter)
        newwords.reverse()
        for x in newwords:
            newstring += x
        return newstring

    def words_to_list(self, words):
        newwords = []
        newstring = ""
        for letter in words:
            newwords.append(letter)
        return newwords

    def twist_block(self, block):
        block_length = len(block)
        if block_length == 3:
            twisted_block = block.pop(2)
            twisted_block += block.pop(0)
            twisted_block += block.pop()
        elif block_length == 2:
            twisted_block = block.pop(1)
            twisted_block += block.pop()
        elif block_length == 1:
            twisted_block = block.pop()
        return twisted_block

    def untwist_block(self, block):
        block_length = len(block)
        if block_length == 3:
            untwisted_block = block.pop(1)
            untwisted_block += block.pop(1)
            untwisted_block += block.pop()
        elif block_length == 2:
            untwisted_block = block.pop(1)
            untwisted_block += block.pop()
        elif block_length == 1:
            untwisted_block = block.pop()
        return untwisted_block

    def block_data(self, words):
        words_length = len(words)
        num_blocks = words_length / 3
        extra_block = words_length % 3
        blocks = []
        block = []
        for ctr, letter in enumerate(words):
            block.append(letter)
            if len(block) == 3:
                blocks.append(block)
                del block
                block = []
            elif extra_block > 0 and ctr == (words_length - 1):
                blocks.append(block)
        return blocks

    def twist(self, data):
        blocks = self.block_data(data)
        cipher_text = ""
        for block in blocks:
            twisted_block = self.twist_block(block)
            cipher_text += twisted_block
        return cipher_text

    def untwist(self, data):
        blocks = self.block_data(data)
        plain_text = ""
        for block in blocks:
            untwisted_block = self.untwist_block(block)
            plain_text += untwisted_block
        return plain_text

class BitChaoX:
    def __init__(self, key, nonce=""):
        self.key = key
        self.nonce = nonce

    def setup(self):
        self.alpha_sub = []
        self.alpha_master = []
        for x in range(256):
            self.alpha_sub.append(x)
            self.alpha_master.append(x)
        for byte in self.key:
            for x in range(ord(byte)):
                self.alpha_sub.append(self.alpha_sub.pop(ord(byte)))
                self.alpha_sub.append(self.alpha_sub.pop(0))
                self.alpha_sub.insert(128,self.alpha_sub.pop(1))
                self.alpha_master.insert(0,self.alpha_master.pop())
                self.alpha_master.insert(0,self.alpha_master.pop(ord(byte)))
                self.alpha_master.insert(128,self.alpha_master.pop())
                self.alpha_sub[x], self.alpha_sub[ord(byte)] = self.alpha_sub[ord(byte)], self.alpha_sub[x]
        if self.nonce != "":
            for byte in self.nonce:
                self.alpha_sub.append(self.alpha_sub.pop(ord(byte)))

    def permute_alpha_sub(self, letter):
        index = self.alpha_sub.index(letter)
        step1 = self.alpha_sub.pop(0)
        self.alpha_sub.insert(index,step1)
        step2 = self.alpha_sub.pop(1)
        self.alpha_sub.insert(128,step2)

    def permute_alpha_master(self, letter):
        index = self.alpha_master.index(letter)
        step1 = self.alpha_master.pop(0)
        self.alpha_master.insert(index,step1)
        step2 = self.alpha_master.pop(0)
        self.alpha_master.append(step2)
        step3 = self.alpha_master.pop(2)
        self.alpha_master.insert(128,step3)

    def encrypt(self, words):
        cipher_text = ""
        self.setup()
        for letter in words:
            char = ord(letter)
            pos = self.alpha_master.index(char)
            sub = self.alpha_sub.pop(pos)
            self.alpha_sub.insert(pos,sub)
            self.permute_alpha_sub(sub)
            self.permute_alpha_master(char)
            cipher_text += chr(sub)
        return cipher_text

    def decrypt(self, words):
        plain_text = ""
        self.setup()
        for letter in words:
            char = ord(letter)
            pos = self.alpha_sub.index(char)
            sub = self.alpha_master.pop(pos)
            self.alpha_master.insert(pos,sub)
            self.permute_alpha_sub(char)
            self.permute_alpha_master(sub)
            plain_text += chr(sub)
        return plain_text

class Polybius:
    def __init__(self, size=5, alphabet=[]):
        self.square = []
        self.squarer = []
        if len(alphabet) == 0:
            schar = 65
            for x in range(26):
                alphabet.append(chr(x + schar))
        c = 0
        schar = 65
        for x in range(1, size + 1):
            row = {}
            rrow = {}
            for y in range(1, size + 1):
                row[y] = alphabet[c]
                rrow[alphabet[c]] = y
                c += 1
                schar += 1
            self.square.append(row)
            self.squarer.append(rrow)

    def getposition(self, letter):
        c = 1
        p = ""
        for row in self.squarer:
            if letter in row.keys():
                p += str(c)
                p += str(row[letter])
            c += 1
        return p

    def getletter(self, pos):
        row = self.square[int(pos[0])-1]
        letter = row[int(pos[1])]
        return letter

    def encrypt(self, data):
        cipher_text = ""
        for c, letter in enumerate(data):
            cipher_text += self.getposition(letter)
            cipher_text += " "
        return cipher_text

    def decrypt(self, data):
        plain_text = ""
        for pos in data.split():
            plain_text += self.getletter(pos)
        return plain_text

class Nihilist:
    def __init__(self, key, size=5):
        self.key = key
        self.size = size
        self.alphabet_size = size * size
        self.alphabet = []
        if size == 6:
            for x in range(26):
                self.alphabet.append(chr(x + 65))
            for x in range(10):
                self.alphabet.append(chr(x + 48))
        elif size == 5:
            for x in range(26):
                if x != 9:
                    self.alphabet.append(chr(x + 65))

    def keysetup(self, key):
        self.square = []
        self.squarer = []
        alphabet = list(self.alphabet)
        keyvals = []
        for letter in key:
            keyvals.append(alphabet.index(letter))
        for val in keyvals:
            for x in range(val):
                alphabet.append(alphabet.pop(val))
                alphabet.append(alphabet.pop(0))
        for x in reversed(range(len(key))):
            alphabet.insert(0,alphabet.pop(alphabet.index(key[x])))
        c = 0
        for x in range(1, self.size + 1):
            row = {}
            rrow = {}
            for y in range(1, self.size + 1):
                row[y] = alphabet[c]
                rrow[alphabet[c]] = y
                c += 1
            self.square.append(row)
            self.squarer.append(rrow)

    def getposition(self, letter):
        c = 1
        p = ""
        for row in self.squarer:
            if letter in row.keys():
                p += str(c)
                p += str(row[letter])
            c += 1
        return p

    def getletter(self, pos):
        row = self.square[int(pos[0])-1]
        letter = row[int(pos[1])]
        return letter

    def encrypt(self, data):
        cipher_text = ""
        self.keysetup(self.key)
        for c, letter in enumerate(data):
            cipher_text += self.getposition(letter)
            cipher_text += " "
        return cipher_text

    def decrypt(self, data):
        plain_text = ""
        self.keysetup(self.key)
        for pos in data.split():
            plain_text += self.getletter(pos)
        return plain_text

class Bifid:
    def __init__(self, size=5, alphabet=[]):
        self.period = size
        self.square = []
        self.squarer = []
        schar = 65
        if len(alphabet) == 0:
            for x in range(26):
                alphabet.append(chr(x + schar))
        c = 0
        for x in range(1, size + 1):
            row = {}
            rrow = {}
            for y in range(1, size + 1):
                row[y] = alphabet[c]
                rrow[alphabet[c]] = y
                c += 1
                schar += 1
            self.square.append(row)
            self.squarer.append(rrow)

    def getposition(self, letter):
        c = 1
        p = ""
        for row in self.squarer:
            if letter in row.keys():
                p += str(c)
                p += str(row[letter])
            c += 1
        return p

    def getletter(self, pos):
        row = self.square[int(pos[0])-1]
        letter = row[int(pos[1])]
        return letter

    def encrypt(self, data):
        cipher_text = ""
        row1 = []
        row2 = []
        for letter in data:
            pos = self.getposition(letter)
            row1.append(pos[0])
            row2.append(pos[1])
        initial = []
        initial2 = []
        for x in range(len(data) / 2):
            first = row1.pop(0)
            second = row1.pop(0)
            initial.append(first+second)
            first = row2.pop(0)
            second = row2.pop(0)
            initial2.append(first+second)
        initial.extend(initial2)
        for i in initial:
            cipher_text += self.getletter(i)
        return cipher_text
    
    def decrypt(self, data):
        plain_text = ""
        values = []
        for letter in data:
            pos = self.getposition(letter)
            values.append(pos[0])
            values.append(pos[1])
        rows = []
        vallen = len(values)
        for r in range(2):
            row = []
            for x in range(vallen / 2):
                row.append(values.pop(0))
            rows.append(row)
        initial = []
        for x in range(len(rows[0])):
            first = rows[0].pop(0)
            second = rows[1].pop(0)
            initial.append(first+second)
        for i in initial:
            plain_text += self.getletter(i)
        return plain_text

class Trifid:
    def __init__(self, key, alphabet=[]):
        self.size = 3
        if len(alphabet) == 0:
            for x in range(65,91):
                alphabet.append(chr(x))
            alphabet.append("+")
        for letter in key:
            alphabet.append(alphabet.pop(0))
            alphabet.append(alphabet.pop(3))
        for letter in key:
            alphabet.append(alphabet.pop(alphabet.index(letter)))
        alphabetb = list(alphabet)
        self.grams = []
        self.gramsr = []
        for x in range(self.size):
            gram = []
            gramr = []
            for r in range(self.size):
                row = {}
                rowr = {}
                for a in range(1,self.size + 1):
                    row[str(a)] = alphabet.pop(0)
                    rowr[alphabetb.pop(0)] = str(a)
                gram.append(row)
                gramr.append(rowr)
            self.grams.append(gram)
            self.gramsr.append(gramr)

    def getposition(self, letter):
        p = ""
        g = 1
        r = 1
        for gram in self.gramsr:
            for row in gram:
                if letter in row.keys():
                    p+= str(g) + str(r) + row[letter]
                r += 1
            g += 1
            r = 1
        return p

    def getletter(self, tri):
        g = int(tri[0]) - 1
        r = int(tri[1]) - 1
        l = tri[2]
        return self.grams[g][r][l]

    def encrypt(self, data):
        cipher_text = ""
        for letter in data:
            cipher_text += self.getposition(letter) + " "
        return cipher_text

    def decrypt(self, data):
        plain_text = ""
        for tri in data.split():
            plain_text += self.getletter(tri)
        return plain_text

class VIC:
    def __init__(self, key="", alphabet=[], delimiter=' ', blanks=[]):
        self.board = []
        alphabet = []
        for x in range(65,91):
            alphabet.append(chr(x))
        alphabet.append(chr(46))
        alphabet.append(chr(47))
        if len(blanks) == 0:
            self.blanks = ['20','60']
        self.delimiter = delimiter
        if len(alphabet) > 0:
            self.alphabet = list(alphabet)
        if len(key) > 0:
            self.keyalphabet(key)
        else:
            self.loadboard()

    def loadboard(self):
        for x in range(10):
            column = []
            for y in range(3):
                pos = str(x) + str(y)
                if pos in self.blanks:
                    column.append(" ")
                else:
                    column.append(self.alphabet.pop(0))
            self.board.append(column)

    def keyalphabet(self, key):
        for letter in key:
            self.alphabet.append(self.alphabet.pop(self.alphabet.index(letter)))
            self.alphabet.append(self.alphabet.pop(0))
            self.alphabet.append(self.alphabet.pop(2))
        self.loadboard()

    def getposition(self, letter):
        pos = ""
        for c, column in enumerate(self.board):
            if letter in column:
                n = column.index(letter)
                if n != 0:
                    if n == 1:
                        n = 2
                    elif n == 2:
                        n = 6
                    pos += str(n) + str(c)
                else:
                    pos += str(c)
        return pos

    def getletter(self, pos):
        if len(pos) == 1:
            letter = self.board[int(pos)][0]
        else:
            if int(pos[0]) == 2:
                row = 1
            elif int(pos[0]) == 6:
                row = 2
            column = int(pos[1])
            letter = self.board[column][row]
        return letter

    def encrypt(self, data):
        cipher_text = ""
        datalen = len(data)
        for c, letter in enumerate(data):
            cipher_text += self.getposition(letter)
            if c != (len(data) - 1):
                cipher_text += self.delimiter
        return cipher_text

    def decrypt(self, data):
        plain_text = ""
        for pos in data.split(self.delimiter):
            if pos != self.delimiter:
                plain_text += self.getletter(pos)
        return plain_text

class Morse:
    morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
    numbers = ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
    morse.extend(numbers)
    alphabet = []
    for x in range(65, 91):
        alphabet.append(chr(x))
    for x in range(48, 58):
        alphabet.append(chr(x))

    def encode(self, data, delimiter=' '):
        buf = ""
        datalen = len(data)
        for c, letter in enumerate(data):
            buf += self.morse[self.alphabet.index(letter)]
            if c != datalen - 1:
                buf += delimiter
        return buf

    def decode(self, data, delimiter=' '):
        buf = ""
        for letter in data.split(delimiter):
            buf += self.alphabet[self.morse.index(letter)]
        return buf

class ADFGX:
    def __init__(self, name=[], alphabet=[]):
        self.square = []
        self.squarer = []
        if len(name) == 0:
            self.name = ['A','D','F','G','X']
        else:
            self.name = name
        self.size = len(self.name)
        self.dictionary = {}
        self.dictionary_rev = {}
        for c, letter in enumerate(self.name):
            self.dictionary[letter] = c
            self.dictionary_rev[c] = letter

        if len(alphabet) == 0:
            schar = 65
            for x in range(26):
                alphabet.append(chr(x + schar))
        c = 0
        for x in range(self.size):
            row = {}
            rrow = {}
            for y in range(self.size):
                row[y] = alphabet[c]
                rrow[alphabet[c]] = y
                c += 1
            self.square.append(row)
            self.squarer.append(rrow)

    def getposition(self, letter):
        p = ""
        for c, row in enumerate(self.squarer):
            if letter in row.keys():
                p += self.dictionary_rev[c]
                p += self.dictionary_rev[row[letter]]
        return p

    def getletter(self, pos):
        r = self.dictionary[pos[0]]
        l = self.dictionary[pos[1]]
        row = self.square[r]
        letter = row[l]
        return letter

    def stage2encrypt(self, stage1, key):
        square = self.transenload(stage1)
        seq = []
        encryption_key = "".join(sorted(key))
        for char in encryption_key:
            seq.append(char)
        for n in seq:
            square.insert(0, square.pop(seq.index(n)))
        cipher_text = ""
        for col in square:
            cipher_text += "".join(col)
        return cipher_text
    
    def stage2decrypt(self, stage1, key):
        square, extras = self.transdeload(stage1)
        seq = []
        encryption_key = "".join(sorted(key))
        for char in encryption_key:
            seq.append(char)
        square.reverse()
        for char in reversed(key):
            seq.insert(0,seq.pop(seq.index(char)))
            square.insert(0, square.pop(seq.index(char)))
        for e in range(len(extras)):
            square[e].append(extras.pop(0))
        cipher_text = ""
        for col in square:
            for x in range(len(col)):
                pos = col.pop(0)
                cipher_text += pos + " "
        return cipher_text

    def transenload(self, data):
        square = []
        column_size = len(data) / self.size
        extra = len(data) % self.size
        c = 0
        for x in range(self.size):
            row = []
            for y in range(column_size):
                row.append(data[c])
                c += 1
            square.append(row)
        last = data[(len(data) - 1) - extra:len(data) - 1]
        extra_list = list(last)
        for e in range(extra):
            square[e].append(extra_list.pop(0))
        return square

    def transdeload(self, data):
        square = []
        column_size = (len(data) / 2) / self.size
        extra = (len(data) / 2) % self.size
        blocks = []
        s = 0
        e = 2
        extras = []
        extracount = 0
        step = (self.size + extra) - 1
        for x in range((len(data) / 2) ):
            if extracount < extra:
                if len(data) > self.size and len(data) < self.size * 2:
                    if x % (self.size + extra) == 0:
                        extras.append(data[s:e])
                        extracount += 1
                        s += 2
                        e += 2
                    else:
                        blocks.append(data[s:e])
                        s += 2
                        e += 2
                elif len(data) < self.size * 2:
                    for x in range(extra):
                        extras.append(data[s:e])
                        s += 2
                        e += 2
            else:
                blocks.append(data[s:e])
                s += 2
                e += 2
        s = self.size
        e = 2
        s = s  - 1
        extra_count = extra
        for x in range(self.size):
            row = []
            for y in range(column_size):
                row.append(blocks.pop(0))
            square.append(row)
        return square, extras

    def stage1encrypt(self, data):
        cipher_text = []
        for c, letter in enumerate(data):
            cipher_text.append(self.getposition(letter))
        return cipher_text

    def stage1decrypt(self, data):
        plain_text = ""
        for pos in data.split():
            plain_text += self.getletter(pos)
        return plain_text

    def encrypt(self, data, key):
        stage1 = self.stage1encrypt(data)
        stage2 = self.stage2encrypt(stage1, key)
        return stage2

    def decrypt(self, data, key):
        stage2 = self.stage2decrypt(data, key)
        stage1 = self.stage1decrypt(stage2)
        return stage1

class ADFGVX(ADFGX):
    def __init__(self, name=['A','D','F','G','V','X'], alphabet=[]):
        if len(alphabet) == 0:
            alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
        self.cipher = ADFGX(name, alphabet)

    def encrypt(self, data, key):
        return self.cipher.encrypt(data, key)

    def decrypt(self, data, key):
        return self.cipher.decrypt(data, key)

class BinaryAffine:
    def __init__(self, a=1000039, ainv=87, b=8):
        self.a = a
        self.ainv = ainv
        self.b = b

    def encrypt(self, data):
        cipher_text = []
        for byte in data:
            sub = ((ord(byte) * self.a) + self.b) % 256
            cipher_text.append(chr(sub))
        return "".join(cipher_text)

    def decrypt(self, data):
        plain_text = []
        for byte in data:
            sub = (self.ainv * (ord(byte) - self.b)) % 256
            plain_text.append(chr(sub))
        return "".join(plain_text)

class AffineCounterMode:
    def __init__(self, a=1000039, ainv=87, b=8):
        self.a = a
        self.ainv = ainv
        self.b = b

    def encrypt(self, data):
        cipher_text = []
        for c, byte in enumerate(data):
            sub = (((ord(byte) * self.a) + c) + self.b) % 256
            cipher_text.append(chr(sub))
        return "".join(cipher_text)

    def decrypt(self, data):
        plain_text = []
        for c, byte in enumerate(data):
            sub = ((self.ainv * ((ord(byte) - c) - self.b))) % 256
            plain_text.append(chr(sub))
        return "".join(plain_text)

class Beaufort:
    def __init__(self, key):
        self.key = list(key)
        self.keylen = len(key)
        self.alphabets = {}
        self.alphabets_rev = {}
        for z, x in enumerate(reversed(range(65,91))):
                alphabet = collections.deque()
                alphabet_dict = {}
                alphabet_dict_rev = {}
                for y in reversed(range(65,91)):
                        alphabet.append(chr(y))
                if z == 0:
                        shift_factor = z
                else:
                        shift_factor = z * -1
                alphabet.rotate(shift_factor)
                for y in reversed(range(65,91)):
                        letter = alphabet.popleft()
                        alphabet_dict[chr(y)] = letter
                        alphabet_dict_rev[letter] = chr(y)
                self.alphabets[chr(x)] = alphabet_dict
                self.alphabets_rev[chr(x)] = alphabet_dict_rev

    def encrypt(self, secret):
        cipher_text = ""
        secret = Atbash().encrypt(secret)
        for x in range(0,len(secret)):
                keyi = self.key[ x % self.keylen]
                sub_dict = self.alphabets[keyi]
                sub = sub_dict[secret[x]]
                cipher_text += sub
        return cipher_text

    def decrypt(self, secret):
        plain_text = ""
        for x in range(0,len(secret)):
                keyi = self.key[ x % self.keylen]
                sub_dict = self.alphabets_rev[keyi]
                sub = sub_dict[secret[x]]
                plain_text += sub
        return Atbash().decrypt(plain_text)

class AutoKeyBeaufort:
    def __init__(self, key):
        self.key = list(key)
        self.keylen = len(key)
        self.alphabets = {}
        self.alphabets_rev = {}
        for z, x in enumerate(reversed(range(65,91))):
                alphabet = collections.deque()
                alphabet_dict = {}
                alphabet_dict_rev = {}
                for y in reversed(range(65,91)):
                        alphabet.append(chr(y))
                if z == 0:
                        shift_factor = z
                else:
                        shift_factor = z * -1
                alphabet.rotate(shift_factor)
                for y in reversed(range(65,91)):
                        letter = alphabet.popleft()
                        alphabet_dict[chr(y)] = letter
                        alphabet_dict_rev[letter] = chr(y)
                self.alphabets[chr(x)] = alphabet_dict
                self.alphabets_rev[chr(x)] = alphabet_dict_rev

    def encrypt(self, secret):
        cipher_text = []
        secret = Atbash().encrypt(secret)
        for k in range(len(secret)):
            keyi = self.key.pop(0)
            sub_dict = self.alphabets[keyi]
            sub = sub_dict[secret[k]]
            self.key.append(secret[k])
            cipher_text.append(sub)
        return "".join(cipher_text)

    def decrypt(self, secret):
        plain_text = []
        for k in range(len(secret)):
            keyi = self.key.pop(0)
            sub_dict = self.alphabets_rev[keyi]
            sub = sub_dict[secret[k]]
            plain_text.append(sub)
            self.key.append(plain_text[k])
        return Atbash().decrypt("".join(plain_text))

class AutoKeyVigenere:
    def __init__(self, key):
        self.key = list(key)
        self.keylen = len(key)
        self.alphabets = {}
        self.alphabets_rev = {}
        for z, x in enumerate(range(65,91)):
                alphabet = collections.deque()
                alphabet_dict = {}
                alphabet_dict_rev = {}
                for y in range(65,91):
                        alphabet.append(chr(y))
                if z == 0:
                        shift_factor = z
                else:
                        shift_factor = z * -1
                alphabet.rotate(shift_factor)
                for y in range(65,91):
                        letter = alphabet.popleft()
                        alphabet_dict[chr(y)] = letter
                        alphabet_dict_rev[letter] = chr(y)
                self.alphabets[chr(x)] = alphabet_dict
                self.alphabets_rev[chr(x)] = alphabet_dict_rev

    def encrypt(self, secret):
        cipher_text = []
        for k in range(len(secret)):
            keyi = self.key.pop(0)
            sub_dict = self.alphabets[keyi]
            sub = sub_dict[secret[k]]
            self.key.append(secret[k])
            cipher_text.append(sub)
        return "".join(cipher_text)

    def decrypt(self, secret):
        plain_text = []
        for k in range(len(secret)):
            keyi = self.key.pop(0)
            sub_dict = self.alphabets_rev[keyi]
            sub = sub_dict[secret[k]]
            plain_text.append(sub)
            self.key.append(plain_text[k])
        return "".join(plain_text)
