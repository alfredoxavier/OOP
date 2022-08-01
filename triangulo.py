import math

class Triangulo(object):
    lados = 3
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c
        self.area = float()
        self.calc_area()
    
    def troca_vertices(self):
      self.A = float(input('Vertice A: '))
      self.B = float(input('Vertice B: '))
      self.C = float(input('Vertice C: '))

    def calc_area(self):
        p = (self.A + self.B + self.C) / 2
        self.area = math.sqrt(p*(p-self.A)*(p-self.B)*(p-self.C))
        # return Area, p