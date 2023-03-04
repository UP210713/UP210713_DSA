class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data

#LIFO = Last Input First Output
#UEPS = Ultimo en Entrar Ultimo en Salir

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmtpy(self):
        return True if self.size == 0 else False
        return True if not self.size else False
        return True if not self.head else False
    
    def push(self, data):
        newNode = Nodo(data)
        newNode.next = self.head
        self.head = newNode
        self.size +=1
        ##TAREA: agregay a Jasus, Maria y Jose y hacer un pop de Jose

    def pop(self):
        dato = None
        if not self.isEmtpy():
            self.size -= 1
            dato = self.head.data
            self.head = self.head.next
        return dato
    
    def peak(self):
        dato = None
        if not self.isEmtpy(): 
            dato = self.head.data
        return dato

    def show (self):
        cadena = ""
        while self.head != None:
            cadena += self.head.data + '-->'
            self.head = self.head.next
        return cadena

pila = Stack()
print(pila.peak())
pila.push("Jesus")
pila.push("Maria")
pila.push("Jose")

print("Sacar --------->")

print(pila.pop())
print(pila.peak())

print('Metodo show')

print(pila.show())

