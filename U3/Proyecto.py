class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

class filaUnidireccional:
        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0
        
        def getSize(self):
            return self.size
    
        def isEmpty(self):
            return True if not self.head else False
        
        def push(self, data):
            newNode = Node(data)
            if self.isEmpty():
                self.head = newNode
                self.tail = newNode
            elif data < self.head.data:
                self.head.previous = newNode
                newNode.next = self.head
                self.head = newNode
            else:
                actual = self.head
                for i in range(self.size):
                    if data < actual.data:
                        newNode.previous = actual.previous
                        newNode.next = actual
                        actual.previous.next = newNode
                        actual.previous = newNode
                        self.size +=1
                        return
                    if actual.next != None:
                        actual = actual.next
                newNode.previous = actual
                actual.next = newNode
                self.tail = newNode
            self.size +=1


        def printRight(self):
            actual = self.head
            lista = []
            for i in range(self.size):
                lista.append(actual.data)
                actual = actual.next
            return lista
        
        def printLeft(self):
            actual = self.tail
            lista = []
            for i in range(self.size):
                lista.append(actual.data)
                actual = actual.previous
            return lista
P = filaUnidireccional()

P.push(5)
P.push(1)
P.push(2)
P.push(4)
P.push(6)

print(P.getSize())
print(P.printRight())
print(P.printLeft())
print(P.tail.data)