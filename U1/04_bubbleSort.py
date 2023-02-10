lista= [8,10,6,2,4]
swapped = True
print("Lista sin ordenar", lista)
while swapped:
    swapped = False
    for i in range (len(lista) -1):
        if lista[i] > lista[i+1]:
            swapped=True
            lista[i], lista[i+1] = lista[i+1], lista[i]

print("Lista ordenada ", lista)