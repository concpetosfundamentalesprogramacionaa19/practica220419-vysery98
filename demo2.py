"""
	Ejemplo de lenguaje Python 2
	autor:@vysery98
"""
import sys

# ingreso de datos
nombre_archivo = sys.argv[0]
valor1 = sys.argv[1]
valor2 = sys.argv[2]

# proceso
suma = int(valor1) + int(valor2) # aquí realizo la suma de variables
multiplicacion = int(valor1) * int(valor2) # aquí realizo el producto de variables

# salida
print("La suma es: %d" % suma)
print("La multiplicación es: %d" % multiplicacion)