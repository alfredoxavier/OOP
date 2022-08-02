from triangulo import Triangulo

a = Triangulo(3,4,5)
print(f'O triangulo "a" possui {a.lados} lados, com os vertices a: {a.A}, b: {a.B} e c: {a.C}, possui área de {a.area} e perímetro de {a.perimetro}')
print('Agora troque os vértices')
a.troca_vertices()
print(f'Agora, o triangulo a possui {a.lados} lados, com os vertices a: {a.A}, b: {a.B} e c: {a.C}, possui nova área de {a.area} e perímetro de {a.perimetro} ')






# Triangulo.A = float(input('Entre com o lado A: '))
# Triangulo.B = float(input('Entre com o lado B: '))
# Triangulo.C = float(input('Entre com o lado C: '))

# # x = Triangulo(Triangulo.A, Triangulo.B, Triangulo.C)
# print(x)

# Area = x.calc_area(Triangulo.A, Triangulo.B, Triangulo.C)
# print(Area)