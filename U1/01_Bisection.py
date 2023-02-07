import math

def Ecuation(num):
    return pow(num, 2) -2

x1= 1
x2= 2
xm= 0
errorEstantadr= 0.001
errorRelativo= abs(x2-x1)
i = 1 
it = round((math.log(x2-x1) -  math.log(errorEstantadr)) / math.log(2))
print("Selected equation: x^2 - 2")
print("Iterations: ",it)
print("i\t|x1\t|x2\t|er\t|xm\t|f(x1)\t|f(xm)\t|f(x1)*f(xm)")

while errorRelativo >= errorEstantadr:
    xm= (x1 + x2) / 2
    print(i,round(x1,3), round(x2,3), round(errorRelativo,3), round(xm,3), round(Ecuation(x1),3), round(Ecuation(xm),3), round((Ecuation(x1)*Ecuation(xm)),3), sep="\t|")
    if Ecuation(x1) * Ecuation(xm) < 0:
        x2 = xm
    else:
        x1 = xm
    errorRelativo= abs (x2-x1)
    i+=1
print("The root is : ", xm)