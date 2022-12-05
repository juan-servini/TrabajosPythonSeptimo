# EJERCICIO 6 

print("Ingrese las coordenadas del punto A: ")
AX=float(input("AX: "))
AY=float(input("AY: "))
print("Ingrese las coordenadas del punto B: ")
BX=float(input("BX: "))
BY=float(input("BY: "))

D=((AX-BX)^2 + (AY-BY)^2)^0.5

print("La distancia entre el punto A y el punto B es: ", D)