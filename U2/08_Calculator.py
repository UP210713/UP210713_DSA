from tkinter import *
from math import *



root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=1, columnspan=10, sticky=W+E)

index=0
def getNumbers(number):
    global index
    display.insert(index, number)
    index += 1
def getOperator(operator):
    global index
    lenghtOperator = len(operator)
    display.insert(index, operator)
    index += lenghtOperator
def clearDisplay():
    display.delete(0, END)
def erease():
    displayState = display.get()
    if len(displayState):
        newDisplay = displayState[:-1]
        clearDisplay()
        display.insert(0, newDisplay)
    else:
        clearDisplay()
        display.insert(0, 'Syntax error')


Q = display.get()
i = 0  

def prioridad(a):
    if a in ['(', ')']:
        return 0
    elif a == '^':
        return 3
    elif a in ['*', '/']:
       return 2
    elif a in ['+', '-']:
        return 1


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

def calculate():
    display_state = display.get()
    try:
        math_expression =  compile(display_state, 'app.py', 'eval')
        result = eval(math_expression)
        clearDisplay()
        display.insert(0,result)
    except:
        clearDisplay()
        display.insert(0,"error")

'''
print(infixToPostfistax(Q))
R=infixToPostfix(Q)
print(postfixToValue(R))
'''

#Botones de la calculadora 
Button(root, text='7', command=lambda:getNumbers(7) ).grid(row=2,column=0)
Button(root, text='8', command=lambda:getNumbers(8) ).grid(row=2,column=1)
Button(root, text='9', command=lambda:getNumbers(9) ).grid(row=2,column=2)

Button(root, text='4', command=lambda:getNumbers(4) ).grid(row=3,column=0)
Button(root, text='5', command=lambda:getNumbers(5) ).grid(row=3,column=1)
Button(root, text='6', command=lambda:getNumbers(6) ).grid(row=3,column=2)

Button(root, text='1', command=lambda:getNumbers(1) ).grid(row=4,column=0)
Button(root, text='2', command=lambda:getNumbers(2) ).grid(row=4,column=1)
Button(root, text='3', command=lambda:getNumbers(3) ).grid(row=4,column=2)
Button(root, text='0', command=lambda:getNumbers(0) ).grid(row=5,column=0)
Button(root, text='AC', command=lambda:clearDisplay() ).grid(row=4,column=5)

Button(root, text='+', command=lambda:getOperator("+") ).grid(row=2,column=4)
Button(root, text='-', command=lambda:getOperator("-") ).grid(row=3,column=4)
Button(root, text='/', command=lambda:getOperator("/") ).grid(row=4,column=4)
Button(root, text='*', command=lambda:getOperator("*") ).grid(row=5,column=4)
Button(root, text='=', command=lambda:calculate() ).grid(row=5,column=2)

Button(root, text='(', command=lambda:getOperator("(") ).grid(row=2,column=5)
Button(root, text=')', command=lambda:getOperator(")") ).grid(row=2,column=6)
Button(root, text='^2', command=lambda:getOperator("**2") ).grid(row=3,column=5)
Button(root, text='DEL', command=lambda:erease()).grid(row=5, column= 5)
Button(root, text='.', command=lambda:getOperator('.') ).grid(row=5,column=1)

root.mainloop()