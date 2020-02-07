"""
1. Napisz skrypt, który będzie wyświetlać wszystkie kolejne dzielniki wprowadzonej liczby
"""

try:
    num = int(input('Enter a number:'))
    for x in range(1, num + 1):
        if num % x == 0:
            print(x)
except ValueError:
    print('You entered a wrong value')