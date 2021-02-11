from KlassiKrypto import Atbash, Affine, Baconian, BaconBits, Polybius, Bifid, Trifid, Caesar, Beale, Chaocipher, Vigenere, Nihilist, Morse, BitChao, BitVigenere, Twist, BitChaoX, VIC, AffineCounterMode, Beaufort, AutoKeyBeaufort, AutoKeyVigenere, ADFGX, ADFGVX

msg = "TEST"
key = "TEST"

ctxt = Affine().encrypt(msg)
ptxt = Affine().decrypt(ctxt)
print(ptxt)

ctxt = Atbash().encrypt(msg)
ptxt = Atbash().decrypt(ctxt)
print(ptxt)

ctxt = BaconBits().encrypt(msg)
ptxt = BaconBits().decrypt(ctxt)
print(ptxt)

ctxt = Baconian().encrypt(msg)
ptxt = Baconian().decrypt(ctxt)
print(ptxt)

ctxt = Chaocipher().encrypt(msg)
ptxt = Chaocipher().decrypt(ctxt)
print(ptxt)

ctxt = Vigenere(key).encrypt(msg)
ptxt = Vigenere(key).decrypt(ctxt)
print(ptxt)

ctxt = BitChao().encrypt(msg)
ptxt = BitChao().decrypt(ctxt)
print(ptxt)

ctxt = Caesar().encrypt(msg)
ptxt = Caesar().decrypt(ctxt)
print(ptxt)

ctxt = BitVigenere(key).encrypt(msg)
ptxt = BitVigenere(key).decrypt(ctxt)
print(ptxt)

ctxt = Twist().encrypt(msg)
ptxt = Twist().decrypt(ctxt)
print(ptxt)

ctxt = BitChaoX(key).encrypt(msg)
ptxt = BitChaoX(key).decrypt(ctxt)
print(ptxt)

ctxt = Polybius().encrypt(msg)
ptxt = Polybius().decrypt(ctxt)
print(ptxt)

ctxt = Nihilist(key).encrypt(msg)
ptxt = Nihilist(key).decrypt(ctxt)
print(ptxt)

ctxt = Bifid().encrypt(msg)
ptxt = Bifid().decrypt(ctxt)
print(ptxt)

ctxt = Trifid(key).encrypt(msg)
ptxt = Trifid(key).decrypt(ctxt)
print(ptxt)

ctxt = VIC(key).encrypt(msg)
ptxt = VIC(key).decrypt(ctxt)
print(ptxt)

ctxt = Morse().encrypt(msg)
ptxt = Morse().decrypt(ctxt)
print(ptxt)

adfgx_msg = "TESTINGTEST"
adfgx_key = "TESTING"

ctxt = ADFGX(adfgx_key).encrypt(adfgx_msg)
ptxt = ADFGX(adfgx_key).decrypt(ctxt)
print(ptxt)

#ctxt = ADFGVX(key).encrypt(msg)
#ptxt = ADFGVX(key).decrypt(ctxt)
#print(ptxt)

ctxt = AffineCounterMode().encrypt(msg)
ptxt = AffineCounterMode().decrypt(ctxt)
print(ptxt)

ctxt = Beaufort(key).encrypt(msg)
ptxt = Beaufort(key).decrypt(ctxt)
print(ptxt)

ctxt = AutoKeyBeaufort(key).encrypt(msg)
ptxt = AutoKeyBeaufort(key).decrypt(ctxt)
print(ptxt)

ctxt = AutoKeyVigenere(key).encrypt(msg)
ptxt = AutoKeyVigenere(key).decrypt(ctxt)
print(ptxt)
