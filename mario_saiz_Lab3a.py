#Author: Mario Saiz
#Class: COSC 1336
#Program: Lab 3a
#Convert certain measurements to other measurements under the same party, from imperial to metric, with some restrictions.

#This will ask for the persons name, and save it under the string "name".
print("\n"*20)
name = input('What is your name?: ')

print("\nAlright, "+ name + ", I know you've been struggling with converting measurements, ")
print("so I wrote a program to help you convert from the imperial system to the ")
print("metric system. Go ahead and pick a number, ONLY 1 through 5, for which ")
print("the measurement you want to convert to, and you'll get the answer for both.")

print('\n(1): Miles to Kilometers? ')
print('(2): Fahrenheit to Celcuis? ')
print('(3): Gallons to Liters? ')
print('(4): Pounds to Kilograms? ') 
print('(5): Inches to Centimeters? ')


#This will save the number they chose into the integer "z".
z = int(input("\nWhat would you like to convert, " + str(name) + "?: "))

#This will convert Miles to Kilometers.
if  z == 1:
    tries = 0
    x = float(input("\nAlright, " + str(name) + ", how many Miles do you want converted into Kilometers?: "))
    #This will end the program if they put anything below zero.
    while (x < 0):
        if tries == 3:
            break
        print("\nValues cannot be negative.")
        print(' ')
        x = float(input("\nAlright, " + str(name) + ", how many Miles do you want converted into Kilometers?: "))
        tries += 1
    if ( x >= 0 ):
        kilometer = float((x*1.6))
        print("\nThere are about, " + str(round(kilometer, 2)) + " kilometer(s) in, " + str(x) + " mile(s).")
        print("Cool!")
    

#This will convert Fahrenheit to Celcuis.
elif  z == 2:
    tries = 0
    x = float(input("\nAlright, " + str(name) + ", how many degrees Fahrenheit do you want converted into degrees Celcuis?: "))
    #This will end the program if they put anything below zero.
    while (x < -1000) or (x > 1000):
        if tries == 3:
            break
        print("\nValues cannot be smaller than -1000 or bigger than 1000.")
        print(' ')
        x = float(input("\nAlright, " + str(name) + ", how many degrees Fahrenheit do you want converted into degrees Celcuis?: "))
        tries += 1
    if ( -1000 <= x <= 1000 ):
        celcius = float(((x-32)*5/9))
        print("\nThere are about, " + str(round(celcius, 1)) + " degree(s) Celcuis in, " + str(x) + " degree(s) Fahrenheit.")
        print("Nice!")


#This will convert Gallons to Liters.
elif  z == 3:
    x = float(input("\nAlright, " + str(name) + ", how many Gallons do you want converted into Liters?: "))
    #This will end the program if they put anything below zero.
    if ( x > 0 ):
        liter = float((x*3.9))
        print("\nThere are about, " + str(round(liter, 2)) + " liter(s) in, " + str(x) + " gallon(s).")
        print("Awesome!")
    else:
         print("\nValues cannot be 0 or a negative.")
         exit()

#This will convert Pounds to Kilograms.
elif  z == 4:
    x = float(input("\nAlright, " + str(name) +  ", how many Pounds do you want converted into Kilograms?: "))
    #This will end the program if they put anything below zero.
    if ( x > 0 ):
         kilogram = float((x*0.45))
         print("\nThere are about, " + str(round(kilogram, 2)) + " kilogram(s) in, " + str(x) +  " pound(s).")
         print("Totally rad!")
    else:
         print("\nValues cannot be 0 or a negative.")
         exit()

#This will convert Inches to Centimeters.
elif  z == 5:
    x = float(input("\nAlright, " + str(name) + ", how many Inches do you want converted into Centimeters?: "))
    #This will end the program if they put anything below zero.
    if ( x > 0 ):
        centimeter = float((x*2.54))
        print("\nThere are about, " + str(round(centimeter, 2)) + " centimeter(s) in, " + str(x) + " inch(es).")
        print("Alright!")
    else:
        print("\nValues cannot be 0 or a negative.")
        exit()

#If the user types a number less than 1 or greater than 5, it'll give an error message and exit out of the program.
else :
     print("\nERROR!")
     exit()







