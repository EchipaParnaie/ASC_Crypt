from itertools import cycle
import argparse

parser = argparse.ArgumentParser(description="Criptare XOR.")
parser.add_argument('key', metavar='parola', type=str, help='Parola de criptare')
parser.add_argument('inputPath', metavar='intrare', type=str, help='Fisierul care contine inputul')
parser.add_argument('outputPath', metavar='iesire', type=str, help='Fisierul care contine outputul')

args = parser.parse_args()
# print(args)

inputFile = outputFile = ''

try:
    inputFile = open(args.inputPath, "r")
except FileNotFoundError:
    print(f"Nu exista fisierul {args.inputPath}!")
    exit(1)

outputFile = open(args.outputPath, "wb")

passwd = str(args.key)  # Citesc parola
s = str(inputFile.read())  # Incarc inputul
crypted = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s, cycle(passwd)))
outputFile.write(crypted.encode("utf8", errors='replace'))
