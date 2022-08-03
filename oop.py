from triangulo import Triangulo

a = Triangulo(3,4,5)
print(f'O triangulo "a" possui {a.lados} lados, com os vertices a: {a.A}, b: {a.B} e c: {a.C}, possui área de {a.area} e perímetro de {a.perimetro}')
print('Agora troque os vértices')
a.troca_vertices()
print(f'Agora, o triangulo a possui {a.lados} lados, com os vertices a: {a.A}, b: {a.B} e c: {a.C}, possui nova área de {a.area} e perímetro de {a.perimetro} ')
a.class_triangulo()
