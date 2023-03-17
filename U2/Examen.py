#Programa 1
listas = [5,2,1,6,3,4,7,9]
corridas = int(input("Cuantos numeros del final, deseas cambiar:\n"))

def rotacion(lista, n):
    for i in range(n):
        nuevoElemento = lista.pop()
        lista.insert(0, nuevoElemento)
    return lista

listaRotada = rotacion(listas,corridas)
print(listaRotada)


#Programa 2


