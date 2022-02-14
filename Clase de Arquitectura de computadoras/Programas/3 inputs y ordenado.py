#Ingresar 3 numeros y ordenarlos

try:
    lista = []
    lista.append(int(input("Ingrese el primer numero: ")))
    lista.append(int(input("Ingrese el segundo numero: ")))
    lista.append(int(input("Ingrese el tercer numero: ")))


#Esta parte del try y except es del Codigo de Abraham que vimos en clase, Gracias :U
except ValueError:
    print("No introdujo un numero awewonao")
 
lista.sort()
print("Tu lista ordenada:" + " ", lista)
