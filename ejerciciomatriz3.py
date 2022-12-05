# EJERCICIO 3 MATRIZ

MONTO = []

print("Ingrese número de sucursales y años: ")
N = int( input("Número de Sucursales: "))
M = int( input("Número de Años: "))

for i in range(M):
    MONTO.append( [] )

MAX = 0
for j in range(N):
    SUMA = 0
for i in range(M):
    SUMA = SUMA + MONTO[i][j]

print ("Número de ventas de la Sucursal" , j+1, "es", SUMA)
if SUMA > MAX :
    MAX = SUMA
    SUC = j + 1

print("Sucursal que más vendió: ", SUC)

MAX = 0
for i in range(M):
    SUMA = 0

for j in range(N):
    SUMA = SUMA + MONTO[i][j]
PROM = SUMA/N
print ("Promedio de ventas del año" , i+1, "es", PROM)

if PROM > MAX :
    MAX = PROM
    AÑO = i + 1

print("Año con mayor promedio: ", AÑO)