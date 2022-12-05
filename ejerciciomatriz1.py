# EJERCICIO 1 MATRIZ

A = []
B = []
C = []

print("Ingrese dimensión de la matriz, máximo 100")
S = int(input("Número de filas: "))
R = int(input("Número de columnas: "))

for i in range(S):
    A.append([])
    B.append([])
    C.append([])
    for j in range(R):
        A[i].append(int(input("A: ".format(i+1j+1))))
        B[i].append(int(input("B: ".format(i+1j+1))))
        C[i].append(A[i][j] + B[i][j])

print(A)
print(B)
print(C)