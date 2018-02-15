# KlassiKrypto - A collection of classical ciphers  
Supported ciphers - Affine, Atbash, Baconian, BaconBits, Chaocipher, BitChao, BitchaoX, Vigenere, BitVigenere, Polybius, Bifid, Trifid, Nihilist, Caesar(rot), Beale, VIC, Morse, ADFGX, ADFGVX, Enimga, Beaufort, AutoKey (Vigenere, Beaufort)  

# Usage:  
msg = "HELLOWORLD"  
key = "HELPME"  

# Affine  
from KlassiKrypto import Affine  
cipher = Affine()  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Atbash  
from KlassiKrypto import Atbash  
cipher = Atbash()  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# BaconBits  
from KlassiKrypto import BaconBits  
cipher = BaconBits()  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Baconian  
from KlassiKrypto import Baconian  
cipher = Baconian()  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Caesar/Rot  
from KlassiKrypto import Caesar  
cipher = Caesar()  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Chaocipher  
from KlassiKrypto import Chaocipher  
cipher = Chaocipher()  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Vigenere  
from KlassiKrypto import Vigenere  
cipher = Vigenere(key)  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# BitChao  
from KlassiKrypto import BitChao  
cipher = BitChao()  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# BitChaoX  
from KlassiKrypto import BitChaoX  
cipher = BitChaoX(key)  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# BitVigenere  
from KlassiKrypto import BitVigenere  
cipher = BitVigenere(key)  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Twist  
from KlassiKrypto import Twist  
cipher = Twist()  
c = cipher.twist(msg)  
p = cipher.untwist(c)  
# Polybius  
from KlassiKrypto import Polybius  
cipher = Polybius()  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Bifid  
from KlassiKrypto import Bifid  
cipher = Bifid()  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Trifid  
from KlassiKrypto import Trifid  
cipher = Trifid(key)  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Nihilist  
from KlassiKrypto import Nihilist  
cipher = Nihilist(key)  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# VIC  
from KlassiKrypto import VIC  
cipher = VIC(key)  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Beale  
from KlassiKrypto import Beale  
cipher = Beale(book)  
c = cipher.encrypt(msg)  
p = cipher.decrypt(c)  
# Morse  
from KlassiKrypto import Morse  
cipher = Morse()  
c = cipher.encode(msg)  
p = cipher.decode(c)  
# ADFGX  
(Currently only supports blocks of 5 characters, input must be evenly divisble by 5)
from KlassiKrypto import ADFGX  
ADFGX().encrypt(data)  
ADFGX().decrypt(data)  
# ADFGVX  
(Currently only supports blocks of 6 characters, input must be evenly divisble by 6)
from KlassiKrypto import ADFGVX  
ADFGVX().encrypt(data)  
ADFGVX().decrypt(data)  
# Enigma  
(Currently only supports the 3 letter Grundstellung setting and plugboard settings.  Ringstellung is not currently supported)  
from KlassiKrypto.enigma import Enigma  
rotor1 = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q"]  
rotor2 = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"]  
rotor3 = ["BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"]  
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  
plugs = ['AC', 'BE']  
settings = "AAA"  

enigma = Enigma(rotor1, rotor2, rotor3, reflector)  
enigma.input(msg, setting, plugs)  
# BinaryAffine  
BinaryAffine().encrypt(data)  
BinaryAffine().decrypt(data)  
# AffineCounterMode  
AffineCounterMode().encrypt(data)  
AffineCounterMode().decrypt(data)  
# Beaufort  
Beaufort(key).encrypt(data)  
Beaufort(key).decrypt(data)  
# AutoKeyVigenere  
AutoKeyVigenere(key).encrypt(data)  
AutoKeyVigenere(key).decrypt(data)  
# AutoKeyBeaufort  
AutoKeyBeaufort(key).encrypt(data)  
AutoKeyBeaufort(key).decrypt(data)  
