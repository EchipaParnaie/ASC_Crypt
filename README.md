# ASC_Crypt

Proiect 1 - Arhitectura Sistemelor de Calcul

Autori: Razvan-Cristian Dumitriu si Andrei-Cristian Murica, grupa 152

## Cum se foloseste?

`python crypt.py parola fisier_intrare fisier_iesire`

Fisierul de intrare va fi in format `.txt`, fisierul de iesire va fi unul binar, fara extensie.

`python decrypt.py parola fisier_intrare fisier_iesire`

Fisierul de intrare va fi un fisier binar, fara extensie, fisierul de iesire va fi in format `.txt`.

### Exemplu

`python crypt.py ParolaMea123 input.txt output`

`python decrypt.py ParolaMea123 output input_recuperat.txt`

## Cum functioneaza criptarea?

Cu ajutorul `argparse` primim si tratam argumentele. Functia `zip` ne ajuta sa cream o pereche `(a,b)`, cu `a` o litera din fisierul de intrare si `b` litera corespunzatoare din parola de criptare. Cu functia `cycle` parcurgem atribuim fiecarei litera din input litera corespunzatoare din parola. Apoi, aplicam XOR intre `ord(a)` si `ord(b)`. 

## Cum functioneaza decriptarea?

Decriptarea functioneaza exact la fel ca si criptarea, singura diferenta fiind intre fisierele de intrare si iesire (intrarea este un fisier binar, outputul este text. Trebuie facuta diferenta intre aceste doua tipuri diferite de fisiere in momentul in care le deschidem - `"w"` pentru text, `"wb"` pentru binar).
