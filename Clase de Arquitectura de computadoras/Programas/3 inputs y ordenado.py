#Ingresar 3 numeros y ordenarlos

lista = []
lista.append(int(input("Ingrese el primer numero: ")))
lista.append(int(input("Ingrese el segundo numero: ")))
lista.append(int(input("Ingrese el tercer numero: ")))

lista.sort()
print("Tu lista ordenada:" + " ", lista)
