"""
12. Utworzyć skrypt z interfejsem tekstowym obliczający n-ty element ciągu Fibonacciego
- wykonać zadanie iteracyjnie i rekurencyjnie
"""


def fib_iteracyjny(x):
    pwyrazy = (0, 1)
    a, b = pwyrazy
    while x > 1:
        a, b = b, a + b
        x -= 1
        return x


x = int(input('Podaj, który element ciągu chcesz policzyć: '))
print(fib_iteracyjny(x))


def fib_rekurencyjny(y):
    a, b = 0, 1
    for i in range(y-1):
        a, b = b, a+b
    return a


y = int(input('Podaj, który element ciągu chcesz policzyć: '))
print(fib_rekurencyjny(y))