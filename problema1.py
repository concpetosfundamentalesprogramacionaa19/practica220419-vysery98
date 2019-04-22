"""
	problema 1
	autor: @vysery98
	programa para calcular el valor mensual a pagar a un trabajador y el valro de su descuento al Seguro Social
"""

# se ingresa los datos por teclado horas trajabadas y el costo hora oficial
horas_trabajadas = input("Ingrese el número de horas trabajadas: ")
costo_oficial = input("Ingrese el valor del costo hora oficial: ")

# proceso: se calcula el suelo / double -> valores decimales
sueldo_trabajador = input(horas_trabajadas) * float(costo_oficial) # producto entre el numero de horas trabajadas por el costo hora
dcto_seguro = float(sueldo_trabajador) * 0.1

# presentación de los datos calculados
print("Valor a mensual a pagar al trabajador: %.2f" % sueldo_trabajador)
print("Valor de su descuento al Seguro Social:%.2f" % dcto_seguro)