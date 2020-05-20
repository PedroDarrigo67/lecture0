from math import sqrt, asin, pi

def area_triangulo(a,b,c):
    s = (a+b+c)/2
    t = sqrt(s*(s-a)*(s-b)*(s-c))
    return t

def angulo_alfa(a,b,c):
    s = area_triangulo (a,b,c)
    t = 180/pi * asin(2 * s/(b*c))
    return t

def menu():
    opcion = 0
    while opcion != 1 and opcion !=2:
        print('1 calcula triangulo')
        print('2 calcula angulo')
        opcion = int(input('escoge opcion'))
    return opcion


resultado = float(0.0)

lado1 = float(input('dame lado a '))
lado2 = float(input('dame lado b '))
lado3 = float(input('dame lado c '))


s = menu()
if s == 1:
    resultado = area_triangulo(lado1 ,lado2 ,lado3)
else:
    resultado = angulo_alfa(lado1 ,lado2 ,lado3)

print('opcion :', s)
print('resultado :', resultado)