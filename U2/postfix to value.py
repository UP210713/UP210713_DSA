i=0
P = [5,6,2,'+','*',12,4,'/','-']
operadores=['+','-','*','/']
pila =[]
P.append(')')
while P[i] != ")":
    if type(P[i]) == int:
        pila.append(P[i])
    elif type(P[i]) == str:
        b= pila.pop()
        a= pila.pop()
        if P[i] == operadores[0]:
            c= a+b
        elif P[i] == operadores[1]:
            c=a-b
        elif P[i] == operadores[2]:
            c = a*b
        elif P[i] == operadores[3]:
            c= a/b
        pila.append(c)
    i += 1    
print(pila)