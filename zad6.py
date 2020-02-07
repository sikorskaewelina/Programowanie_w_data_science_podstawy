"""
6. Utwórz skrypt dodający ułamki zwykłe
"""


try:
    licznik1 = float(input('Podaj licznik pierwszego ułamka: '))

    mianownik1 = float(input('Podaj mianownik pierwszego ułamka: '))
    if mianownik1 == 0:
        print('Sprzeczność')

    licznik2 = float(input('Podaj licznik drugiego ułamka: '))

    mianownik2 = float(input('Podaj mianownik drugiego ułamka: '))
    if mianownik2 == 0:
        print('Sprzeczność')

    mianownik3 = int(mianownik1 * mianownik2)
    if mianownik3 == 0:
        print('Sprzeczność')

    licznik3 = int((mianownik3 / mianownik1) * licznik1 + (mianownik3 / mianownik2) * licznik2)
    print(licznik3, '/', mianownik3)

except ValueError:
        print('Podałeś złą wartość')