class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

#FIFO = PEPS

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return True if not self.head else False
    
    def enQueue(self,data):
        newNode = Node(data)
        self.size +=1
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
    def deQueue(self):
        if not self.isEmpty():
            old = self.headlf
            if self.size == 1:
                self.tail = None
            self.size -= 1
            data = self.head.data
            self.head = self.head.next
            del old
            return data
        else:
            return None
    
    def deQueue2(self):
        data = None
        if not self.isEmpty():
            self.size -= 1
            old = self.head
            data = self.head.data
            self.head = self.head.next
            del old
            if self.isEmpty():
                self.tail = None
        return data
    
    def show(self):
        datos = ''
        id = self.head
        for i in range(0, self.size):
            datos += str(id.data) + '<='
            id = id.next
        return datos

#Hacer que funcione el show y hacer el serch


q = Queue()
print(q.getSize())
q.enQueue(5)
q.enQueue(9)
q.enQueue(8)
#Metodo enqueue
print(q.head.data)
print(q.head.next.data)
print(q.tail.data)
#Metodo show
print( q.show())