from turtle import Vec2D


print("Vector3:")

print("Ingrese numero de elementos de vector")

N=int(input())

if 1 <=N and N <=200:

    for i in range(1,N+1):
        elemento = int(input("Ingrese Entero {0}: ".format(i)))
        Vec2D.append(elemento)

i=0

lista_nueva =[]

for elemento in Vec2D:

    if elemento not in lista_nueva:
     lista_nueva.append(elemento)

lista_nueva.sort() 

print("\nSALIDA:")
print(lista_nueva)