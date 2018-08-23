from KlassiKrypto.enigma import Enigma
#from enigmamachine import Enigma
import sys, select, time

setting = "AAA"
plugs = ""

if select.select([sys.stdin,],[],[],0.0)[0]:
    data = sys.stdin.read()
    data = data[:len(data) - 1]
else:
    setting = raw_input("Enter setting: ")
    plugs = raw_input("Enter plugs: ")
    data = raw_input("Enter text: ")

rotor1_set = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q"]
rotor2_set = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"]
rotor3_set = ["BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"]
reflector_set = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

start = time.time()
enigma = Enigma(rotor1_set, rotor2_set, rotor3_set, reflector_set)
sys.stdout.write(enigma.input(data, setting, list(plugs.split()))+"\n")
end = time.time() - start
bps = len(data) / end
sys.stderr.write("Completed in "+str(end)+" seconds\n")
sys.stderr.write(str(bps)+" bytes per second.\n")
