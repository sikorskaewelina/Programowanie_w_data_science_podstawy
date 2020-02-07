"""
8. W klasie przeprowadzono sprawdzian, za który uczniowie mogli otrzymać maksymalnie 40 punktów.
Skala ocen w szkole jest następująca:
0-39% - ndst,
40-49% - dop,
50-69% - dst,
70-84% - db,
85-99% - bdb,
100% - cel.
Utwórz skrypt z interfejsem tekstowym, który na podstawie podanej liczby punktów ze sprawdzianu
wyświetli ocenę jaka się należy (skorzystaj z konstrukcji if, elif, else)
"""


x = float(input('Podaj liczbę puntów: '))
if x == 40:
    print('cel')
elif 34 <= x <= 39.9:
    print('bdb')
elif 28 <= x <= 33.9:
    print('db')
elif 20 <= x <= 27.9:
    print('dst')
elif 16 <= x <= 19.9:
    print('dop')
else:
    print('ndst')


