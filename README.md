# ASC_Crypt

Proiect 1 - Arhitectura Sistemelor de Calcul

Autori: Razvan-Cristian Dumitriu si Andrei-Cristian Murica, grupa 152

## Cum se foloseste?

`python crypt.py fisier_parola fisier_intrare fisier_iesire`

`python decrypt.py fisier_parola fisier_intrare fisier_iesire`

### Exemplu

`python crypt.py parola.txt input.txt output`

`python decrypt.py parola.txt output input_recuperat.txt`

## Cum functioneaza criptarea?

Cu ajutorul `argparse` primim si tratam argumentele. Functia `zip` ne ajuta sa cream o pereche `(a,b)`, cu `a` o litera din fisierul de intrare si `b` litera corespunzatoare din parola de criptare. Apoi, aplicam XOR intre `ord(a)` si `ord(b)`. Rezultatul va fi un numar in baza 2 pe 8 biti, pe care il afisam in fisierul de iesire.

## Cum functioneaza decriptarea?

Tot cu ajutorul `argparse` primim si tratam argumentele. Fisierul de intrare de data aceasta va fi un sir binar, nu un text, ca la criptare, asa ca impartim sirul binar din fisierul de intrare in grupe de 8 biti. Cu ajutorul functiei `int` transformam fiecare grupa de 8 biti intr-un numar zecimal, apoi aplicam XOR cu `ord(b)`, `b` fiind litera corespunzatoare grupei din parola. Rezultatul va fi un numar zecimal, pe care il transformam in litera cu ajutorul functiei `chr`, apoi il afisam in fisierul de iesire.
