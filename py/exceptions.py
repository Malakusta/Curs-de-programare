import sys

try:
    x = int(input("Introduceti un numar: "))
    y = int(input("Introduceti un alt numar: "))
except ValueError:
    print("Eroare: Trebuie sa introduceti numere intregi valide.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Eroare: Impartirea la zero nu este permisa.")
    sys.exit(1)


print("Rezultatul impartirii este:", result)