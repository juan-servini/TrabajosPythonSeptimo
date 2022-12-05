# EJERCICIO 13

año=int(input("Ingrese año: "))

if (año % 4) or (año % 100 == 0) and (año % 400 != 0):
    print("El año es bisiesto")
else:
    print("El año NO es bisiesto")