"""
	Ejemplo de lenguaje Python 3
	autor:@vysery98
"""
# entrada de datos: Valor 1 y Valor 2
valor1 = input("Ingrese el valor 1: ")
valor2 = input("Ingrese el valor 2: ")

# proceso
suma = int(valor1) + int(valor2) # aquí realizo la suma de variables
multiplicacion = int(valor1) * int(valor2) # aquí realizo el producto de variables

# presentación
print("La suma es: %d.\tLa multiplicación es: %d" % (suma, multiplicacion))