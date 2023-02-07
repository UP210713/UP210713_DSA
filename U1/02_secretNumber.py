import random

secretNumber=random.randint(0,60)
win=False
while win==False:
    num=int(input("Give one number: \n"))
    if num<secretNumber:
        print("Give me a higher number")
    elif num>secretNumber:
        print("Give me a lower number")
    elif num==secretNumber:
        print("Corretly, the number is equal!")
        win=True