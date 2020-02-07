"""
31. Korzystając z instrukcji np.random.choice oraz reshape z pakietu numpy 
stworzyć funkcję generują macierz kwadratową stopnia N wypełnioną wartościami 
0 i 255 w losowy sposób
"""

import numpy as np


def matrix(n):
    return np.random.choice(np.array([0, 255]), (n,n))


n = 10
print(matrix(n))