from itertools import cycle
import argparse

parser = argparse.ArgumentParser(description="Criptare XOR.")
parser.add_argument('key', metavar='parola', type=str, help='Parola de decriptare')
parser.add_argument('inputPath', metavar='intrare', type=str, help='Fisierul care contine inputul')
parser.add_argument('outputPath', metavar='iesire', type=str, help='Fisierul care contine outputul')

args = parser.parse_args()
# print(args)

inputFile = outputFile = ''

try:
    inputFile = open(args.inputPath, "rb")
except FileNotFoundError:
    print(f"Nu exista fisierul {args.inputPath}!")
    exit(1)

outputFile = open(args.outputPath, "w")

passwd = str(args.key)  # Citesc parola
s = str(inputFile.read().decode("utf8"))  # Incarc inputul
decrypted = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s, cycle(passwd)))
outputFile.write(decrypted)
