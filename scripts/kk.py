from KlassiKrypto.tools import Ciphers
from KlassiKrypto import Atbash, Affine, Baconian, BaconBits, Polybius, Bifid, Trifid, Caesar, Beale, Chaocipher, Vigenere, Nihilist, ADFGX, ADFGVX
import getpass, sys

def usage():
    sys.stdout.write("Usage: python kk.py <algorithm> <encrypt/decrypt> <optional key>\n")
    sys.exit(0)

if len(sys.argv) <= 1:
    usage()

if sys.argv[1] == "list":
    sys.stdout.write("Supported ciphers:\n")
    sys.stdout.write("------------------\n")
    c = Ciphers(Atbash).list()
    for a in c:
        sys.stdout.write(a+"\n")
    sys.exit(0)

try:
    algorithm = sys.argv[1]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

try:
    mode = sys.argv[2]
except IndexError as ier:
    print "Error: Did you forget encrypt/decrypt?"
    sys.exit(1)

if algorithm in Ciphers(Atbash).keyed_ciphers:
    try:
        key = sys.argv[3]
    except IndexError as ier:
        key = getpass.getpass("Enter key: ")
else:
    key = ""

try:
    data = sys.argv[4]
except IndexError as ier:
    data = ""

if mode == "encrypt":
    if data == "":
        data = raw_input("Enter text to encrypt: ")
    c = Ciphers(eval(algorithm)).encrypt(data, key)
    sys.stdout.write(c+"\n")
elif mode == "decrypt":
    if data == "":
        data = raw_input("Enter text to decrypt: ")
    p = Ciphers(eval(algorithm)).decrypt(data, key)
    sys.stdout.write(p+"\n")
