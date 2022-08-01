from triangulo import triangulo

triangulo.A = float(input('Entre com o lado A: '))
triangulo.B = float(input('Entre com o lado B: '))
triangulo.C = float(input('Entre com o lado C: '))

x = triangulo()
y = triangulo()

Area = x.Area(triangulo.A, triangulo.B, triangulo.C)
print(Area)
