"""
. Utwórz klasę Prostokąt, a następnie na jej podstawie (korzystając z 
mechanizmu dziedziczenia) utwórz klasę Kwadrat
"""


class Prostokat:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def pole(self):
        p = self.a * self.b
        return p
    
    def obwod(self):
        obw = self.a*2 + self.b*2
        return obw
    
class Kwadrat(Prostokat):
    def __init__(self,a,b):
        super().__init__(a,b)
        
    def opisz(self):
        if self.a==self.b:
            print("Kwadrat")
        else:
            print("Prostokąt")
            
            
figura=Kwadrat(1,2)
figura.pole()
figura.obwod()
figura.opisz()

figura1=Kwadrat(2,2)
figura1.pole()
figura1.obwod()
figura1.opisz()