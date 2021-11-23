from itertools import cycle

keyFile = inputFile = outputFile = ''
try:
    keyFile = open("parola", "r")
except FileNotFoundError:
    print("Nu exista fisierul parola!")
    exit(1)

try:
    inputFile = open("output", "r")
except FileNotFoundError:
    print("Nu exista fisierul input.txt!")
    exit(1)

outputFile = open("input.txt", "w")

passwd = keyFile.readline()  # Citesc parola
aux = inputFile.read()
s = [aux[i:i + 8] for i in range(0, len(aux), 8)]
for a, b in zip(s, cycle(passwd)):
    print(chr((int(a, 2) ^ ord(b))), end='')
