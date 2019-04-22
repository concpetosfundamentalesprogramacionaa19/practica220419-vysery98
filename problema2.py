"""
	problema 1
	autor: @vysery98
	programa para cacular el valor de "m", en base a los datos "x,y,z" ingresados por teclado.
"""

# se ingresa los datos por teclado de x, y, z
x = input("Ingrese el valor correspondiente a \"x\": ")
y = input("Ingrese el valor correspondiente a \"y\": ")
z = input("Ingrese el valor correspondiente a \"z\": ")

# proceso: se calcula el valor de m, todos los datos seran de tipo float
m = (float(x) + (float(y)/float(z)))/(float(x) - (float(y)/float(z)))

# salida de datos
print("El valor de m, en base a las variables:\nx = %.2f\n\ty = %.2f\n\t\tz = %.2f\nda como resultado:\n\t\t\tm = %.2f" % (float(x), float(y), float(z), float(m)))