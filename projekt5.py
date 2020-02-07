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

titanic_data = pd.read_csv(r"/Users/ewelina/Desktop/CDV/I_semestr/Programowanie_w_data_science_podstawy/titanic/train.csv")
titanic_data.head()

"""
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S
"""

survived = titanic_data[titanic_data.Survived ==0]

survived['Sex'].hist() 
#Prawie pięć razy więcej umarło meżczyzn niż kobiet

survived['Age'].hist()
#Najwięcej osób zmarło w przedziale wiekowym od 15 do 30 lat

survived['Pclass'].hist()
#Ponad 3,5 raza więcej osób zmarło z niższej klasy społecznej niż z średnej lub wyższej
