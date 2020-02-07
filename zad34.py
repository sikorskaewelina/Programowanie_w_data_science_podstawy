"""
34. Utwórz klasę Kwadrat z konstruktorem ustalającym jego bok oraz metodami: 
    wyświetlającymi wartość tego boku, obliczającymi pole i obwód figury
"""

class Kwadrat():
    def __init__(self, a):
        self.a = a
        
    def bok(self):
        return "Kwadrat o boku {}".format(self.a)
    
    def pole(self):
        return "polu {}".format(self.a**2)
    
    def obwod(self):
        return "i obwodzie {}".format(self.a*4)
    

k=Kwadrat(5)
print(k.bok())   
print(k.pole())  
print(k.obwod())
