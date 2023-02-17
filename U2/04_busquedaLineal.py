def linearNotSort(lista, n):
    lista
    a= False
    i=0
    while a is False and i < len(lista):
        if lista[i] == n:
            a = True
        i += 1
    if a is True:
        return i-1
    else:
        return None

def linearSort(lista2,n2):
    lista2
    a= False
    i=0
    while a is False and i < len(lista2) and lista2[i] <= n:
        if lista2[i] == n:
            a = True
        i += 1
    if a is True:
        return i-1
    else:
        return None

lista =[-5,2,3,6,1,9,14]
lista2 = [-3,0,5,7,9,10,14]
n=int(input("Dame un numero cualquiera:\n"))
n2=int(input("Dame un numero cualquiera:\n"))
print("El numero se encuentra en la posicion:\n",linearNotSort(lista,n))
print("El numero se encuentra en la posicion:\n",linearSort(lista2,n2))