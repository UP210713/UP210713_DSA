Q = ['(',5,'*','(',6,'+',2,')','/',12,'-',4,')']
P = []
Pila = []
i = 0 
while Q[i] == ['(','*','+','/','-',')']:
    '''
    if type(P[i]) == int:
        P.append(Q[i])
    elif type(P[i]) == str:
        Pila.append(Q[i])
    i += 1
    '''
print(Pila)
print(P)