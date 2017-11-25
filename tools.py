from KlassiKrypto import Atbash, Affine, Baconian, BaconBits, Polybius, Bifid, Trifid, Caesar, Beale, Chaocipher, Vigenere, Nihilist, Morse
class Ciphers:
    ciphers = ['Atbash', 'Affine','Baconian','BaconBits','Polybius','Bifid', 'Trifid','Caesar','Beale', 'Chaocipher']
    keyed_ciphers = ['Vigenere','Nihilist','Morse']
    ciphers.extend(keyed_ciphers)

    def __init__(self, cipher):
        c = str(cipher).split('.')[1]
        if c in self.ciphers:
            self.cipher = cipher
        else:
            raise ValueError('Error: Cipher not supported')

    def list(self):
        return sorted(self.ciphers)

    def encrypt(self, data, key=""):
        if str(self.cipher).split('.')[1] in self.keyed_ciphers:
            return self.cipher(key).encrypt(data)
        else:
            return self.cipher().encrypt(data)

    def decrypt(self, data, key=""):
        if str(self.cipher).split('.')[1] in self.keyed_ciphers:
            return self.cipher(key).decrypt(data)
        else:
            return self.cipher().decrypt(data)
