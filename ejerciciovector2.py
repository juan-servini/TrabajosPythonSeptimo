# EJERCICIO VECTOR 2

suma = 0
media = 0.0
c = 0
temp = []

print("Ingrese cantidad de temperaturas: ")
N = int(input())

for i in range(N):
    temperatura = float(input("Ingrese tempertura: ".format(i+1)))
    temp.append(temperatura)
    suma = suma + temp[i]
    media = suma/N

for tempElement in temp:
    if tempElement >= media:
        c = c + 1
        print(tempElement)

print("La media es: ", media)
print("Total de temperaturas mayor o igual a la media es: ", c)
