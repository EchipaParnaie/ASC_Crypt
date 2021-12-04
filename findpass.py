inputFile = outputFile = ''

try:
    inputFile = open("input.txt", "r")
except FileNotFoundError:
    print("Nu exista fisierul input.txt!")
    exit(1)

try:
    outputFile = open("output", "rb")
except FileNotFoundError:
    print("Nu exista fisierul output!")
    exit(1)

passFile = open("parola", "w")

s1 = inputFile.read()
s2 = outputFile.read().decode()

result = [chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2)]

if len(result) <= 10:
    print(''.join(x for x in result))
    exit(0)

for i in range(10, 16):
    if result[:i] == result[i:2 * i]:
        print(''.join(x for x in result[:i]))
        exit(0)
