inputFile = open("output", "rb")

alphabet = ['\n', ' ', '!', '"', "'", ',', '-', '.', ':', ';', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

inputText = inputFile.read().decode("utf8")
for passlen in range(10, 16):
    passwd = [-1] * passlen
    for i in range(passlen):
        for c in alphabet[11:]:
            curr = i
            ok = True
            while curr < len(inputText) and ok:
                if chr(ord(c) ^ ord(inputText[curr])) not in alphabet:
                    ok = False
                curr += passlen
            if ok:
                passwd[i] = c
    if passwd != [-1] * passlen:
        print(''.join(str(x) for x in passwd))
        exit(0)
