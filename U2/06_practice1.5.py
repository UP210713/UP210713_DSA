import random

listaRandom = random.sample(range(100,500), 100)
value=int(input("Dime que numero quieres buscar:\n"))
c=0

def bubbleSort (lista):
    swapped = True
    print("Lista sin ordenar\n", lista)
    while swapped:
        swapped = False
        for i in range (len(lista) -1):
            if lista[i] > lista[i+1]:
                swapped=True
                lista[i], lista[i+1] = lista[i+1], lista[i]

def binarySearch(lista, valor):
    c = 0
    inicio = 0
    final = len(lista)
    mid = ( inicio + final)//2
    while inicio <= final and lista[mid] != valor:
        if valor < lista[mid]:
            final = mid -1
        else:
            inicio = mid + 1
        mid = (inicio + final)//2
        c += 1
    if lista[mid] == valor:
        return mid, c
    else:
        return None

def quickSort(a, primero, ultimo):
    central = (primero+ultimo)//2
    pivote = a[central]
    i = primero
    j =ultimo
    while True:
        while a[i] < pivote:
            i += 1
        while a[j] > pivote:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        if i > j:
            break
        if primero <= j:
            quickSort(a,primero,j)
        elif i < ultimo:
            quickSort(a,i,ultimo)
        return a

bubbleSort(listaRandom)
print("Lista ordenada")
print(listaRandom)
print(quickSort(listaRandom, 0, 99))
print("Lista convertida en matriz:\n")
for c, i in enumerate(listaRandom):
    if c%10 == 0:
        print()
    print(i, end=' ')
print('\n')
print("Posicion del valor buscado:\n",binarySearch(listaRandom, value))

