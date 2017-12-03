class Rotor:
    def __init__(self, alphabet, notch):
        self.alphabet = list(alphabet)
        self.notch = notch
        self.position = 0
        self.counter = 0

class Wiring:
    def __init__(self, rotor1, rotor2, rotor3):
        self.rotor1 = Rotor(rotor1[0], rotor1[1])
        self.rotor2 = Rotor(rotor2[0], rotor2[1])
        self.rotor3 = Rotor(rotor3[0], rotor3[1])
        self.etw = [chr(i) for i in range(65,91)]

    def rotor1_input(self, char):
        p = ((ord(char) - 65) + self.rotor1.position) % 26
        r = (p - self.rotor2.position) % 26
        sub = chr((((ord(self.rotor1.alphabet[r]) - 65) - self.rotor1.position) % 26) + 65)
        sub = self.rotor1.alphabet[r]
        sub = chr((((ord(sub) - 65) - self.rotor1.position) % 26) + 65)
        return sub

    def rotor1_output(self, char):
        b = chr((((ord(char) - 65) + self.rotor1.position) % 26) + 65)
        sub = chr((self.rotor1.alphabet.index(b)+ 65))
        return sub

    def rotor2_input(self, char):
        self.step(2)
        p = ((ord(char) - 65) - self.rotor3.position) % 26
        s = (p + self.rotor2.position) % 26
        sub = self.rotor2.alphabet[s]
        return sub

    def rotor2_output(self, char):
        r = chr((((ord(char) - 65) + self.rotor2.position) % 26) + 65)
        p = chr((((ord(r) - 65) - self.rotor1.position) % 26) + 65)
        sub = chr((self.rotor2.alphabet.index(p) + 65))
        return sub
    
    def rotor3_input(self, char):
        self.step(3)
        pos = ((ord(char) - 65) + self.rotor3.position) % 26
        p = (pos - self.rotor2.position) % 26
        sub = self.rotor3.alphabet[pos]
        return sub

    def rotor3_output(self, char):
        sub = chr((((ord(char) - 65) + self.rotor3.position) % 26) + 65)
        sub = chr((((ord(sub) - 65) - self.rotor2.position) % 26) + 65)
        sub = chr(self.rotor3.alphabet.index(sub) + 65)
        sub = chr((((ord(sub) - 65) - self.rotor3.position) % 26) + 65)
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

    def program_wiring(self, setting):
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
    wiring = {'A':'A', 'B':'B', 'C':'C', 'D':'D','E':'E','F':'F','G':'G','H':'H','I':'I','J':'J','K':'K','L':'L','M':'M','N':'N','O':'O','P':'P','Q':'Q','R':'R','S':'S','T':'T','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z':'Z' }
    def __init__(self, config):
            for pair in config:
                one = pair[0]
                two = pair[1]
                self.wiring[one] = two
                self.wiring[two] = one

    def input(self, char):
        return self.wiring[char]

class Reflector:
    def __init__(self, config):
        self.alphabet = list(config)

    def input(self, char):
        return self.alphabet[(ord(char) - 65)]

class Enigma:
    def __init__(self, rotor1, rotor2, rotor3, reflector):
        self.wiring = Wiring(rotor1, rotor2, rotor3)
        self.reflector = Reflector(reflector)

    def input(self, data, ringsetting="AAA", setting="AAA", plugboard=""):
        buf = []
        plugboard = Plugboard(plugboard)
        self.wiring.program_wiring(ringsetting.upper())
        msg = "".join(data.split())
        for letter in msg.upper():
            sub = plugboard.input(letter)
            sub = self.wiring.rotor3_input(sub)
            sub = self.wiring.rotor2_input(sub)
            sub = self.wiring.rotor1_input(sub)
            sub = self.reflector.input(sub)
            sub = self.wiring.rotor1_output(sub)
            sub = self.wiring.rotor2_output(sub)
            sub = self.wiring.rotor3_output(sub)
            sub = plugboard.input(sub)
            buf.append(sub)
        return "".join(buf)
