from itertools import cycle
import argparse

parser = argparse.ArgumentParser(description="Criptare XOR.")
parser.add_argument('keyPath', metavar='parola', type=str, help='Fisierul care contine parola')
parser.add_argument('inputPath', metavar='intrare', type=str, help='Fisierul care contine inputul')
parser.add_argument('outputPath', metavar='iesire', type=str, help='Fisierul care contine outputul')

args = parser.parse_args()
# print(args)

keyFile = inputFile = outputFile = ''
try:
    keyFile = open(args.keyPath, "r")
except FileNotFoundError:
    print("Nu exista fisierul parola!")
    exit(1)

try:
    inputFile = open(args.inputPath, "r")
except FileNotFoundError:
    print("Nu exista fisierul input.txt!")
    exit(1)

outputFile = open(args.outputPath, "w")

passwd = keyFile.readline()  # Citesc parola
aux = inputFile.read()
s = [aux[i:i + 8] for i in range(0, len(aux), 8)]
for a, b in zip(s, cycle(passwd)):
    outputFile.write(chr((int(a, 2) ^ ord(b))))
