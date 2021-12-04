# ASC_Crypt

Proiect 0x00 - Arhitectura Sistemelor de Calcul

Autori: Razvan-Cristian Dumitriu si Andrei-Cristian Murica, grupa 152

## Cum se foloseste?


### Pentru criptare:

`python crypt.py parola fisier_intrare fisier_iesire`

Fisierul de intrare va fi in format `.txt`, fisierul de iesire va fi unul binar, fara extensie.


### Pentru decriptare:

`python decrypt.py parola fisier_intrare fisier_iesire`

Fisierul de intrare va fi un fisier binar, fara extensie, fisierul de iesire va fi in format `.txt`.

### Exemplu:

`python crypt.py ParolaMea123 input.txt output`

`python decrypt.py ParolaMea123 output input_recuperat.txt`

## Cum functioneaza criptarea?

Cu ajutorul `argparse` primim si tratam argumentele. Functia `zip` ne ajuta sa cream o pereche `(a,b)`, cu `a` o litera din fisierul de intrare si `b` litera corespunzatoare din parola de criptare. Cu functia `cycle` parcurgem atribuim fiecarei litera din input litera corespunzatoare din parola. Apoi, aplicam XOR intre `ord(a)` si `ord(b)`. 

## Cum functioneaza decriptarea?

Decriptarea functioneaza exact la fel ca si criptarea, singura diferenta fiind intre fisierele de intrare si iesire (intrarea este un fisier binar, outputul este text. Trebuie facuta diferenta intre aceste doua tipuri diferite de fisiere in momentul in care le deschidem - `"w"`, respectiv `"r"` pentru text, `"wb"`, respectiv `"rb"` pentru binar).

# Partea a 2-a:

Pentru continuarea proiectului, Echipa Parnaie (formata din Razvan-Cristian Dumitriu si Andrei-Cristian Murica de la grupa 152) versus echipa [Edge](https://github.com/Edge0410/Proiect-ASC-0x00). Cheia echipei Edge este `ParolaASC1`.

# Probleme intalnite:

Din motive pe care nu le-am putut intelege, programele ruleaza gresit in momentul in care copiem si lipim textul output al echipei adverse. In schimb, daca rulam direct codul echipei adverse pe fisierele input/output, programele functioneaza as-expected. Presupunem ca, din cauza formatului neconventional in care este furnizat outputul se pierd anumite caractere la copy-paste, sau mai exista varianta in care echipa adversa nu a furnizat cum trebuie fisierul output.

# Explicarea rezolvarii:

Am conceput doua programe Python: `findpass.py` si `findpass_brute.py`. Vom explica mai jos cum functioneaza fiecare dintre ele.

## `findpass.py`:

Acest program foloseste fisierele `input.txt` si `output` ale echipei adverse si aplica operatia XOR intre caracterele din ele, grupandu-le cu ajutorul functiei `zip`. Astfel, in lista `result` vom obtine cheia initiala de decriptare, ce se va repeta pentru fiecare caracter din fisierul de intrare/iesire. Apoi, stiind ca cheia de decriptare va avea intre 10 si 15 caractere, programul va scoate din `result` cheia de decriptare si o va afisa pe ecran.

### Cum se foloseste?

Programul functioneaza intr-un singur mod, fara a lua argumente la apel. Astfel, utilizand comanda `python findpass.py`, programul va lua fisierele `input.txt` si `output`, pe care le considera deja existente si va afisa parola de decriptare in consola.

## `findpass_brute.py`:

Acest program se foloseste strict de fisierul binar `output` al echipei adverse si gaseste cheia initiala de criptare, dupa urmatorul principiu: stim ca fisierul initial este un fisier text, continand litere mari, litere mici, cifre, semne de punctuatie si caractere albe (spatii, `\n`-uri). Stocam aceste caractere in lista `alphabet`. Astfel, programul cauta cheia de lungime 10-15 caractere alfanumerice astfel incat aplicand XOR fisierului `output` cu aceasta cheie sa obtinem un text lizibil, care contine doar caractere aflate in `alphabet`. Odata gasita, cheia initiala va fi afisata pe ecran.

### Cum se foloseste?

Acest program functioneaza tot intr-un singur mod, fara a primi argumente la apel. Utilizand comanda `python findpass_brute.py`, programul va lua fisierul binar `output` pe care il considera deja existent si va afisa parola initiala de criptare in consola.
