#ingrese el inicio de la serie : 10
#ingrese el fin de la serie : 100
#imprimir las listas:
#lista = [10, 11, 12, 13, 14.........]
#de la lista original vamos a sacar 2 sublista : impares y pares
#imprimir por pantalla ambas listas tanto de pares como de impares.
#range(0,0,8) :




n1 = int(input("Valor 1 \t"))
n2 = int(input("Valor 2 \t"))

listA = []
listB = []

lista = list(range(n1, n2+1))

for i in lista:
    if i%2 == 0:
        listA.append(i)
    else:
        listB.append(i)
print (lista)
print (listA)
print (listB)
