
def prioridad(a):
    if a in ['(', ')']:
        return 0
    elif a == '^':
        return 3
    elif a in ['*', '/']:
       return 2
    elif a in ['+', '-']:
        return 1


Q = ['5','*','(','6','+','2',')','-','12','/','4',]
Q.insert(0, '(')
Q.append(')')
i = 0  

def infixToPostfix(Q): 
    P = []
    Pila = []  

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
            P.append(int(Q[i]))
    P.append(')')
    return P

def postfixToValue(P):
    i=0
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
    return pila

print(infixToPostfix(Q))
R=infixToPostfix(Q)
print(postfixToValue(R))