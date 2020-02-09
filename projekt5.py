"""
5. Zapoznaj się z danymi dotyczącymi ofiar katastrofy Titanica. W oparciu 
o artykuł zawarty na stronie: 
    
https://stackabuse.com/pandas-library-for-data-visualization-in-python/ 

wykonaj analizę pliku z danymi. Przedstaw dane w postaci tabeli, sporządź 
histogram wieku ofiar, odpowiedz na pytanie - co mogło mieć wpływ na przeżycie 
pasażerów (płeć, wiek, status posłeczny na podstawie klasy biletu).
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv(r"/Users/ewelina/Desktop/CDV/I_semestr/zaliczenie_python/titanic/train.csv")
print(titanic)

"""
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
"""

survived = titanic[titanic.Survived ==0]
survived['Age'].hist()

print(titanic.groupby('Sex')['Survived'].mean())
"""
Sex
female    0.742038
male      0.188908

Na przeżycie pasażerów wpływ miała między innyi płeć. Prawie siedemdziesięciu 
pięciu procentom kobiet spośród wszystkich pasażerów płci żeńskiej udało się 
przyżyć katastrofę, natomiast mężczyzn przeżyło zaledwie niecałe 19% spośród 
wszystkich pasażerów płci męskiej.
"""

print(titanic.groupby('Pclass')['Survived'].mean())
"""
Pclass
1    0.629630
2    0.472826
3    0.242363

Wplyw na przeżycie miał również status społeczny. Im wyższy status tym większy
odsetek osób, które przetrwały katastrofę. Im wyższa klasa społeczna tym ok 20%
większe przeżycie. 
"""

print(titanic.pivot_table('Survived', 'Sex', 'Pclass'))
"""
Pclass         1         2         3
Sex                                 
female  0.968085  0.921053  0.500000
male    0.368852  0.157407  0.135447

Najwększe przeżycie było wśród kobiet z klasy wyższej (97% ocalałych) 
i średniej (92% ocalałych). Kobiety w klasie niższej miały zaledwie 50% 
przeżywalność. W zdecydowanie gorszej sytuacji znaleźli się mężczyźni. Około 
35% mężczyzn z klasy wyższej przetrwało katastrofę. W klasie średniej i niższej 
odsetek ocalałych mężczyzn wynosił kolejno około 15% oraz 13,5%.
"""

age = pd.cut(titanic['Age'], [0,17,100])
print(titanic.pivot_table('Survived', ['Sex', age]))
"""
                  Survived
Sex    Age                
female (0, 17]    0.690909
       (17, 100]  0.771845
male   (0, 17]    0.396552
       (17, 100]  0.177215

Jeżeli chodzi o wiek to nie miał on dużego wpływu na przeżycie pasażerów płuci 
żeńskiej, natomiast w przeżyciu mężczyzn odrygwał znaczącą rolę. Ponad dwa razy 
więcej ocalałych mężczyzn to osoby poniżej 17 roku życia.
"""











