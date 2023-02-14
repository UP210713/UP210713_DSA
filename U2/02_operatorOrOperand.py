def prioridad(a):
    if a in ['(', ')']:
        return 4
    elif a == '^':
        return 3
    elif a in ['*', '/']:
       return 2
    elif a in ['+', '-']:
        return 1

P = [5,6,2,'+','*',12,4,'/','-']
for i in P:
    try:
        float(i)
        print(f"{i} Es un operando")
    except ValueError:
        if i in ['+','-','*','/','^','(',')']:
            print(f"{i} Es un operador, con un nivel de prioridad de: ", prioridad(i))
        else:
            print(f"{i} Es un caracter")