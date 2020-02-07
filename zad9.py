"""
9. Utwórz skrypt z interfejsem tekstowym, który wyliczy sumę n kolejnych liczb
(użytkownik podaje pierwszą i ostatnią liczbę sumy).
Uwaga - w zadaniu należy zbudować funkcję własną realizującą dane zadanie
"""


def suma(a, b):
    y=0
    for x in range(a, b+1):
        y=y+x
    return y


a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj ostatnią liczbę: '))
print(suma(a, b))