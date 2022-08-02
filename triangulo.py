import math

class Triangulo(object):
    lados = 3
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c
        self.area = float()
        self.perimetro = float()
        self.calc_area()
        self.calc_perimetro()
          
    def troca_vertices(self):
      try:
        self.A = float(input('Vertice A: '))
        self.B = float(input('Vertice B: '))
        self.C = float(input('Vertice C: '))
        self.calc_area()
        self.calc_perimetro()
      
      except(ValueError):
        print('Os lados dos triangulo devem ser numeros!')
        ans = (input('Deseja tentar novamente (S/N)'))
        ans = ans.upper()
        if ans == ('S'):
          self.troca_vertices() 
        elif ans == ('N'):
          print('Cancelado pelo usuário')
        else:
          print('Resposta incorreta')

    def calc_area(self):
        p = (self.A + self.B + self.C) / 2
        self.area = math.sqrt(p*(p-self.A)*(p-self.B)*(p-self.C))
        # return Area, p

    def calc_perimetro(self):
      self.perimetro = self.A + self.B + self.C