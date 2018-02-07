def genalphabet(alphabet):
    a = []
    for letter in alphabet:
        a.append(ord(letter) - 65)
    return a

class Rotor:
    def __init__(self, alphabet, notch):
        self.alphabet = genalphabet(alphabet)
        self.notch = notch
        self.position = 0
        self.counter = 0

class Wiring:
    def __init__(self, rotor1, rotor2, rotor3):
        self.rotor1 = Rotor(rotor1[0], rotor1[1])
        self.rotor2 = Rotor(rotor2[0], rotor2[1])
        self.rotor3 = Rotor(rotor3[0], rotor3[1])
        self.etw = [chr(i) for i in range(65,91)]
        self.chars = {}
        self.chars_rev = {}
        for x in range(26):
            self.chars[x] = chr(x + 65)
            self.chars_rev[chr(x + 65)] = x

    def rotor1_input(self, char):
        p = (char + self.rotor1.position) % 26
        r = (p - self.rotor2.position) % 26
        sub = ((self.rotor1.alphabet[r]) - self.rotor1.position) % 26
        sub = self.rotor1.alphabet[r]
        sub = (sub - self.rotor1.position) % 26
        return sub

    def rotor1_output(self, char):
        b = (char + self.rotor1.position) % 26
        sub = self.rotor1.alphabet.index(b)
        return sub

    def rotor2_input(self, char):
        self.step(2)
        p = (char - self.rotor3.position) % 26
        s = (p + self.rotor2.position) % 26
        sub = self.rotor2.alphabet[s]
        return sub

    def rotor2_output(self, char):
        r = (char + self.rotor2.position) % 26
        p = (r - self.rotor1.position) % 26
        sub = self.rotor2.alphabet.index(p)
        return sub
    
    def rotor3_input(self, char):
        self.step(3)
        pos = (char + self.rotor3.position) % 26
        p = (pos - self.rotor2.position) % 26
        sub = self.rotor3.alphabet[pos]
        return sub

    def rotor3_output(self, char):
        sub = (char + self.rotor3.position) % 26
        sub = (sub - self.rotor2.position) % 26
        sub = self.rotor3.alphabet.index(sub)
        sub = (sub - self.rotor3.position) % 26
        return sub

    def step(self, num):
        if num == 3:
            self.rotor3.position = (self.rotor3.position + 1) % 26
        if num == 2:
            for notch in self.rotor3.notch:
                if self.rotor3.position + 65 == (ord(notch) + 1):
                    self.rotor2.position = (self.rotor2.position + 1) % 26
            for notch in self.rotor2.notch:
                if self.rotor2.position + 65 == (ord(self.rotor2.notch)) and self.rotor2.counter == 1:
                    self.rotor1.position = (self.rotor1.position + 1) % 26
                    self.rotor2.position = (self.rotor2.position + 1) % 26
                    self.rotor2.counter += 1
                if self.rotor2.position + 65 == (ord(self.rotor2.notch)) and (self.rotor2.counter == 2 or self.rotor2.counter > 26):
                    self.rotor2.counter = 0
                if self.rotor2.position + 65 == (ord(self.rotor2.notch)) and (self.rotor2.counter == 0 or self.rotor2.counter > 26):
                    self.rotor2.counter = 1

    def program_wiring(self, setting, rsetting):
        self.rotor1.counter = 0
        self.rotor1.position = 0
        self.rotor2.counter = 0
        self.rotor2.position = 0
        self.rotor3.position = 0
        self.rotor3.counter = 0
        for x in range((ord(setting[0]) - 65)):
            self.rotor1.position = (self.rotor1.position + 1) % 26
        for x in range((ord(setting[1]) - 65)):
            self.rotor2.position = (self.rotor2.position + 1) % 26
        for x in range((ord(setting[2]) - 65)):
            self.rotor3.position = (self.rotor3.position + 1) % 26

class Plugboard:
    wiring = {}
    for x in range(26):
        wiring[x] = x

    def __init__(self, config):
            for pair in config:
                one = pair[0]
                two = pair[1]
                self.wiring[ord(one) - 65] = ord(two) - 65
                self.wiring[ord(two) - 65] = ord(one) - 65

    def input(self, char):
        return self.wiring[char]

class Reflector:
    def __init__(self, config):
        self.alphabet = genalphabet(config)

    def input(self, char):
        return self.alphabet[char]

class Enigma:
    def __init__(self, rotor1, rotor2, rotor3, reflector):
        self.wiring = Wiring(rotor1, rotor2, rotor3)
        self.reflector = Reflector(reflector)

    def input(self, data, ringsetting="AAA", setting="AAA", plugboard=""):
        buf = []
        plugboard = Plugboard(plugboard)
        self.wiring.program_wiring(ringsetting.upper(), setting)
        msg = "".join(data.split())
        for letter in msg.upper():
            c = self.wiring.chars_rev[letter]
            sub = plugboard.input(c)
            sub = self.wiring.rotor3_input(sub)
            sub = self.wiring.rotor2_input(sub)
            sub = self.wiring.rotor1_input(sub)
            sub = self.reflector.input(sub)
            sub = self.wiring.rotor1_output(sub)
            sub = self.wiring.rotor2_output(sub)
            sub = self.wiring.rotor3_output(sub)
            sub = plugboard.input(sub)
            buf.append(self.wiring.chars[sub])
        return "".join(buf)
