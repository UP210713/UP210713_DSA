Q = ['5','*','(','6','+','2',')','/','12','-','4',]
P = []
##[5,6,2,'+','*',12,4,'/','-']
Pila = []
i = 0 
Q.insert(0, '(')
Q.append(')')
def prioridad(a):
    if a in ['(', ')']:
        return 0
    elif a == '^':
        return 3
    elif a in ['*', '/']:
       return 2
    elif a in ['+', '-']:
        return 1
    
for i in range (len(Q)):
    if Q[i] == '(':
        
        Pila.append(Q[i])
        
    elif Q[i] in ['+', '-', '*','/', '^']:
        if prioridad(Q[i]) <= prioridad(Pila[len(Pila)-1]):
            P.append(Pila.pop())
        Pila.append(Q[i])
    elif Q[i] == ')':
        j = len(Pila)-1
        while Pila[j] != '(':
            P.append(Pila.pop())
            j-=1
        Pila.pop()
    else:
        P.append(Q[i])
print(P)