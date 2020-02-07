"""
13. Utworzyć skrypt z interfejsem tekstowym obliczający symbol Newtona n po k.
Utworzyć funkcję, która będzie wywoływać inną funkcję
"""


def newton(n, k):
    x = 1
    for i in range(1, k + 1):
        x = x * (n - i + 1) / i
    return x


n = int(input('Podaj liczbę n: '))
k = int(input('Podaj liczbę k: '))

if n == k or k == 0:
    print('1')
elif n > k:
    print(newton(n, k))
else:
    print('Błąd, n mniejsze niż k')