Q = ['5','*','(','6','+','2',')','/','12','-','4',]
P = []
##[5,6,2,'+','*',12,4,'/','-']
Pila = []
i = 0 
Q.insert(0, '(')
Q.append(')')

for i in range (len(Q)):
    if Q[i] == '(':
        
        Pila.append(Q[i])
        
    elif Q[i] in ['+', '-', '*','/', '^']:
        Pila.append(Q[i])
    elif Q[i] == ')':
        while i in range(len(P)):
            P = Pila.pop()
            if P[i] == '(':
                Pila.pop()
                break
    else:
        P.append(Q[i])
print(P)