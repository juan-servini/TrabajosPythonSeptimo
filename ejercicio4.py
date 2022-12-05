# EJERCICIO 4

print("Ingrese la cantidad de partidos ganados")
PG=int(input())
print("Ingrese la cantidad de partidos perdidos")
PP=int(input())
print("Ingrese la cantidad de partidos empatados")
PE=int(input())

PPG= PG * 3
PPP= PP * 0
PPE= PE * 1
PF= PPG + PPP + PPE

print("El puntaje final es: ", PF)
