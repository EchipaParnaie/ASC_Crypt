from itertools import cycle # Test

keyFile = inputFile = outputFile = ''
try:
    keyFile = open("parola", "r")
except FileNotFoundError:
    print("Nu exista fisierul parola!")
    exit(1)

try:
    inputFile = open("input.txt", "r")
except FileNotFoundError:
    print("Nu exista fisierul input.txt!")
    exit(1)

outputFile = open("output", "w")

passwd = keyFile.readline()  # Citesc parola
s = inputFile.read()  # Incarc inputul
for a, b in zip(s, cycle(passwd)):
    outputFile.write(format((ord(a) ^ ord(b)), '08b'))  # Aplic XOR si afisez pe 8 biti
