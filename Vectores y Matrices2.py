print("Vector2: ")

Suma = 0
Media = 0
C = 0
Temp=[]

print("Ingrese cantidad de Temperaturas: ")
N=int(input())

for i in range(N):
    Temperatura = float(input("Ingrese Temperatura {0}:".format(i+1)))
    Temp.append(Temperatura)
    Suma=Suma + Temp[i]

media=Suma/N

for tempElement in Temp:
    if tempElement>=Media:
        C=C+1
        print(tempElement)

print("\nSalida")
print("La media es", Media)
print("Total temperaturas>= a la media es", C)        