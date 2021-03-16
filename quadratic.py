# Mario Saiz

import math

print("Quadratic Formula - Mario Saiz")
print("----------------------------------")

a = float(input("What is the value of a? "))
b = float(input("What is the value of b? "))
c = float(input("What is the value of c? "))

sqrt = (b**2)-(4*a*c)
imagine = sqrt*-1
rootable = False
imaginerootable = False

for i in range(0,100):
    if  sqrt == i**2:
        rootable = True
        break
    elif sqrt == i**2*-1:
        imaginerootable = True
        break

if a == 0:
    for i in range (0,1000):
        print("Not quadratic try again")
    
elif sqrt <0:
    print("\nImaginary\nPositive: (",-b, "+ Sqrt(",sqrt,")) / ", 2*a)
    print("Negative: (",-b,"- Sqrt(",sqrt,")) / ", 2*a)
    cont = input("\nWould you like to simplify the imaginary Number?(y/n) ")
    if cont == "y" or cont == "yes" or cont == "yea" or cont == "yeah":
        perform = input("Would you like me to perform the sqrt?(y/n) ")
        if perform == "y" or perform == "yes":
            print("\nPositive: ",format((-b+math.sqrt(sqrt*-1))/(2*a),',.2f'),"i",sep="")
            print("Negative: ",format((-b-math.sqrt(sqrt*-1))/(2*a),',.2f'),"i",sep="")
        elif imaginerootable == True and b%(a*2) == 0:
            print("\nPositive: -",format(math.sqrt(imagine),',.2f'),"i",sep="")
            print("Negative: ",format(math.sqrt(imagine),',.2f'),"i",sep="")
        elif imaginerootable == True:
            print("\nPostitive: (",-b," + ",format(math.sqrt(imagine),',.2f'),"i) / ", 2*a, sep="")
            print("Negative: (",-b," - ",format(math.sqrt(imagine),',.2f'),"i) / ", 2*a, sep="")
        elif b%(a*2) == 0:
            simple = b/(a*2)
            print("\nPositive: -sqrt(",format(imagine,',.2f'),"i)",sep="")
            print("Negative: sqrt(",format(imagine,',.2f'),"i)",sep="")
        else :
            print("\nPositive: ( ",-b," + sqrt( ",format(imagine,',.2f'),"i )) / ", 2*a, sep="")
            print("Negative: ( ",-b," - sqrt( ",format(imagine,',.2f'),"i )) / ", 2*a, sep="")

elif sqrt >= 0:
    print("\nNot imaginary\nPositive: (",-b, "+ Sqrt(",sqrt,")) / ", 2*a)
    print("Negative: (",-b,"- Sqrt(",sqrt,")) / ", 2*a)
    cont = input("\nWould you like to simplify the formula?(y/n) ")

    if cont == "y" or cont == "yes":
        perform = input("Would you like me to perform the sqrt?(y/n) ")
        if perform == "y" or perform == "yes":
            print("\nPositive: ",format((-b+math.sqrt(sqrt*-1))/(2*a),',.2f'),"i",sep="")
            print("Negative: ",format((-b-math.sqrt(sqrt*-1))/(2*a),',.2f'),"i",sep="")
        
        elif rootable == True and b%(a*2) == 0.0:
            print("Positive: -",format(math.sqrt(sqrt),',.2f'),sep="")
            print("Negative: ",format(math.sqrt(sqrt),',.2f'),sep="")
        
        elif rootable == True:
            pquadratic = (-b+math.sqrt(sqrt))/(2*a)
            nquadratic = (-b-math.sqrt(sqrt))/(2*a)
            print("Positive:",format(pquadratic, ',.2f'),"\nNegative:",format(nquadratic, ',.2f'))
        
        elif b%(a*2) == 0.0:
            print("Positive: -sqrt(",format(sqrt,',.2f'),")",sep="")
            print("Negative: sqrt(",format(sqrt,',.2f'),")",sep="")

        else :
            print("\nPositive: ( ",-b," + sqrt( ",format(sqrt,',.2f')," )) / ", 2*a, sep="")
            print("Negative: ( ",-b," - sqrt( ",format(sqrt,',.2f')," )) / ", 2*a, sep="")
        
else :
    print("Magical bug?")
