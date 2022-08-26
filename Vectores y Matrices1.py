print("Vector1: lectura de N elementos enteros")

i=1
F=[]

print("ingrese numero de elementos a ingrensa: ")
numElementos = int(input())

while i<= numElementos:
    elemento=int(input("ingrese Elemento: "))
    F.append(elemento)

    i=i+1
print("\nSALIDA") 
print(F)   
