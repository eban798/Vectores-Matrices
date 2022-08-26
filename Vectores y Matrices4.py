print("Matriz1: SUMA DE MATRICES")

A=[]
B=[]
C=[]

print("ingrese dimension de la matriz, máximo 100")
S=int(input("Numero de Filas:"))
R=int(input("Numero Columnas:"))

for i in range(S):
    A.append([])
    B.append([])
    C.append([])
    for j in range(R):
        A[i].append(int(input("A{}{}:".format(i+1,j+1))))
        B[i].append(int(input("B{}{}:".format(i+1,j+1))))
        C[i].append(A[i][j] +B[i][j])

print("\nSALIDA:")
print(A)
print(B)
print(C)