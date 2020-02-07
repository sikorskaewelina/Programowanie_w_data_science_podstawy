"""
4. Utwórz klasę Martix. Wykorzystaj całą wiedzę jaką posiadasz na temat 
macierzy. Zdefiniuj wszystkie znane Ci operacje.
"""

class Martix:
    def __init__(self, wiersze, kolumny):
        self.wiersze = wiersze 
        self.kolumny = kolumny 
    
    def użytkownik_wypełnia(self): 
        self.body = []
        for i in range(self.wiersze):
            init_list = []
            for j in range(self.kolumny):
                element = float(input("aij = "))
                init_list.append(element)
            self.body.append(init_list)
            
    def macierz_z_zerami(self):
        self.body = []
        for i in range(self.wiersze):
            init_list = []
            for j in range(self.kolumny):
                element = 0
                init_list.append(element)
            self.body.append(init_list)
            
    def macierz_z_jedynkami(self): 
        self.body = []
        for i in range(self.wiersze):
            init_list = []
            for j in range(self.kolumny):
                element = 1
                init_list.append(element)
            self.body.append(init_list)
            
    def macierz_jednostkowa(self):
        if(self.wiersze == self.kolumny):
            self.body = []
            for i in range(self.wiersze):
                init_list = []
                for j in range(self.kolumny):
                    if (i==j):
                        element = 1
                    else:
                        element = 0
                    init_list.append(element)
                self.body.append(init_list)
        else:
            print("Liczba wierszy różni się od liczby kolumn.")
            
    def dodawanie(self, other):
        if(self.kolumny == other.kolumny and self.wiersze == other.wiersze and len(self.body) != 0 and len(other.body) != 0):
            for i in range(self.wiersze):
                for j in range(self.kolumny):
                    self.body[i][j] = self.body[i][j] + other.body[i][j]
        else:
            print("Liczba wierszy różni się od liczby kolumn.")
            
    def odejmowanie(self, other):
        if(self.kolumny == other.kolumny and self.wiersze == other.wiersze and len(self.body) != 0 and len(other.body) != 0):
            for i in range(self.wiersze):
                for j in range(self.kolumny):
                    self.body[i][j] = self.body[i][j] - other.body[i][j]  
        else:
            print("Liczba wierszy różni się od liczby kolumn.")
            
    def mnożenie_przez_macierz(self, other):
        if(self.kolumny == other.kolumny and self.wiersze == other.wiersze and len(self.body) != 0 and len(other.body) != 0):
            for i in range(self.wiersze):
                for j in range(self.kolumny):
                    self.body[i][j] = self.body[i][j] * other.body[i][j]
                    
    def mnożenie_przez_liczbe(self, a):
        for i in range(self.wiersze):
            for j in range(self.kolumny):
                self.body[i][j] = a*self.body[i][j]            

    def wypisz(self):
        print(self.body)
        