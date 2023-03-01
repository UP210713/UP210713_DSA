class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

nodo1 = Nodo("Jesus")
print(nodo1.data)
print(nodo1.getData())
print(nodo1.next)   

nodo1.setData("Maria")
print(nodo1.getData())
print(nodo1.data)

nodo2 = Nodo("Jose")
nodo1.next = nodo2

nodo3 = Nodo("Jesus")
nodo2.next = nodo3

print("-------------->")
print(nodo1.data)
print(nodo1.next.data)
print(nodo1.next.next.data)