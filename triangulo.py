import math

class triangulo():
    A = float()
    B = float()
    C = float()
    
    def Area(self, A, B, C):
        p = (A + B + C) / 2
        Area = math.sqrt(p*(p-A)*(p-B)*(p-C))
        return Area, p
    