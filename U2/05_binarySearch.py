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

lista2 = [-3,0,1,5,7,9]
valor5 = int(input("Dame un numero: "))
print(binarySearch(lista2, valor5))
