#Author: Mario Saiz
#Class: COSC 1336
#Program: Lab 5a
#Instantiate classes, and call them up, modifying assignment Lab 4a, with loops and tries, plus extra credit

print("\n"*20)
name = input("What is your name?: ")


def USorUK():
    tries = 0

    choice = int(input("\nWould you like to convert from US to UK (1), or UK to US (2)?: "))

    if (choice == 1):
        print("\nAlright, "+ str(name) + ", I know you've been struggling with converting measurements, ")
        print("so I wrote a program to help you convert from the IMPERIAL system to the ")
        print("METRIC system. Go ahead and pick a number, ONLY 1 through 5, for which ")
        print("the measurement you want to convert to, and you'll get the answer for both.")

        print('\n(1): Miles to Kilometers? ')
        print('(2): Fahrenheit to Celcuis? ')
        print('(3): Gallons to Liters? ')
        print('(4): Pounds to Kilograms? ') 
        print('(5): Inches to Centimeters? ')


        option = int(input("\nPlease choose an option, 1 - 5: "))


    elif (choice == 2):
        print("\nLet's do this, "+ str(name) + ", I know you've been struggling with converting measurements, ")
        print("so I wrote a program to help you convert from the METRIC system to the ")
        print("IMPERIAL system. Go ahead and pick a number, ONLY 6 through 10, for which ")
        print("the measurement you want to convert to, and you'll get the answer for both.")

        print('\n(6): Kilometers to Miles? ')
        print('(7): Celcius to Fahrenheit? ')
        print('(8): Liters to Gallons? ')
        print('(9): Kilograms to Pounds? ') 
        print('(10): Centimeters to Inches? ')


        option = int(input("\nPlease choose an option, 6 - 10: "))



    
#---------------------
    if (option == 1):
        miles = float(input("\nAlright, " + str(name) + ", how many Miles do you want converted into Kilometers?: "))
        while (miles < 0):
            if tries == 3:
                break
            print("\nValues cannot be negative.")
            print(' ')
            miles = float(input("\nAlright, " + str(name) + ", how many Miles do you want converted into Kilometers?: "))
            tries += 1
        milesToKm(miles)

#----------------------
    elif (option == 2):
        fahrenheit = float(input("\nAlright, " + str(name) + ", how many degrees Fahrenheit do you want converted into degrees Celsuis?: "))
        while (fahrenheit < -1000) or (fahrenheit > 1000):
            if tries == 3:
                break
            print("\nValues cannot be smaller than -1000 or bigger than 1000.")
            print(' ')
            fahrenheit = float(input("\nAlright, " + str(name) + ", how many degrees Fahrenheit do you want converted into degrees Celsuis?: "))
            tries += 1
        FahToCel(fahrenheit)

#-------------------------
    elif (option == 3):
        gallons = float(input("\nAlright, " + str(name) + ", how many Gallons do you want converted into Liters?: "))
        while ( gallons < 0 ):
            if tries == 3:
                break
            print("\nValues cannot be 0 or a negative.")
            print(" ")
            gallons = float(input("\nAlright, " + str(name) + ", how many Gallons do you want converted into Liters?: "))
            tries += 1
        GalToLit(gallons)

#------------------------
    elif (option == 4):
        pounds = float(input("\nAlright, " + str(name) +  ", how many Pounds do you want converted into Kilograms?: "))
        while ( pounds < 0 ):
            if tries == 3:
                break
            print("\nValues cannot be 0 or a negative.")
            print(" ")
            pounds = float(input("\nAlright, " + str(name) +  ", how many Pounds do you want converted into Kilograms?: "))
            tries += 1
        PoundsToKg(pounds)

#------------------------
    elif (option == 5):
        inches = float(input("\nAlright, " + str(name) + ", how many Inches do you want converted into Centimeters?: "))
        while ( inches < 0 ):
            if tries == 3:
                break
            print("\nValues cannot be 0 or a negative.")
            print(" ")
            inches = float(input("\nAlright, " + str(name) + ", how many Inches do you want converted into Centimeters?: "))
            tries += 1
        InchesToCm(inches)

#----------------------
#----------------------
    elif (option == 6):
        kilometers = float(input("\nAlright, " + str(name) + ", how many Kilometers do you want converted into Miles?: "))
        while (kilometers < 0):
            if tries == 3:
                break
            print("\nValues cannot be negative.")
            print(' ')
            kilometers = float(input("\nAlright, " + str(name) + ", how many Kilometers do you want converted into miles?: "))
            tries += 1
        KmToMiles(kilometers)

#----------------------
    elif (option == 7):
        celcuis = float(input("\nAlright, " + str(name) + ", how many degrees Celsius do you want converted into degrees Fahrenheit?: "))
        while (celsius < -1000) or (celsius > 1000):
            if tries == 3:
                break
            print("\nValues cannot be smaller than -1000 or bigger than 1000.")
            print(' ')
            celsius = float(input("\nAlright, " + str(name) + ", how many degrees Celsius do you want converted into degrees Fahrenheit?: "))
            tries += 1
        CelToFah(celsius)

#----------------------
    elif (option == 8):
        liters = float(input("\nAlright, " + str(name) + ", how many Liters do you want converted into Gallons?: "))
        while ( liters < 0 ):
            if tries == 3:
                break
            print("\nValues cannot be 0 or a negative.")
            print(" ")
            liters = float(input("\nAlright, " + str(name) + ", how many Liters do you want converted into Gallons?: "))
            tries += 1
        LitToGal(liters)

#------------------------
    elif (option == 9):
        kilograms = float(input("\nAlright, " + str(name) +  ", how many Kilograms do you want converted into Pounds?: "))
        while ( kilograms < 0 ):
            if tries == 3:
                break
            print("\nValues cannot be 0 or a negative.")
            print(" ")
            kilograms = float(input("\nAlright, " + str(name) +  ", how many Kilograms do you want converted into Pounds?: "))
            tries += 1
        KgToPounds(kilograms)

#-----------------------
    elif (option == 10):
        centimeters = float(input("\nAlright, " + str(name) + ", how many Centimeters do you want converted into Inches?: "))
        while ( centimeters < 0 ):
            if tries == 3:
                break
            print("\nValues cannot be 0 or a negative.")
            print(" ")
            centimeters = float(input("\nAlright, " + str(name) + ", how many Centimeters do you want converted into Inches?: "))
            tries += 1
        CmToInches(centimeters)

    else:
        print("Error, value is not 1 - 10!")
        exit()

#-----------------------------------------------------------------------------------------------------------------------------------------------


def milesToKm(miles):
    if ( miles >= 0 ):
        kilometer = float((miles*1.6))
        print("\nThere are about, " + str(round(kilometer, 2)) + " kilometer(s) in, " + str(miles) + " mile(s).")
        print("Cool!")


def FahToCel(fahrenheit):
    if ( -1000 <= fahrenheit <= 1000 ):
        celsius = float(((fahrenheit-32)*5/9))
        print("\nThere are about, " + str(round(celsius, 1)) + " degree(s) Celsuis in, " + str(fahrenheit) + " degree(s) Fahrenheit.")
        print("Nice!")



def GalToLit(gallons):
    if ( gallons > 0 ):
        liter = float((gallons*3.9))
        print("\nThere are about, " + str(round(liter, 2)) + " liter(s) in, " + str(gallons) + " gallon(s).")
        print("Awesome!")



def PoundsToKg(pounds):
    if ( pounds > 0):
         kilogram = float((pounds*0.45))
         print("\nThere are about, " + str(round(kilogram, 2)) + " kilogram(s) in, " + str(pounds) +  " pound(s).")
         print("Totally rad!")



def InchesToCm(inches):
    if ( inches > 0):
        centimeter = float((inches*2.54))
        print("\nThere are about, " + str(round(centimeter, 2)) + " centimeter(s) in, " + str(inches) + " inch(es).")
        print("Alright!")

#-------------------------------------
#-------------------------------------

def KmToMiles(kilometers):
    if ( kilometers >= 0 ):
        miles = float((kilometers/1.6))
        print("\nThere are about, " + str(round(miles, 2)) + " mile(s) in, " + str(kilometers) + " kilometer(s).")
        print("Cool!")


def CelToFah(celsuis):
    if ( -1000 <= celsius <= 1000 ):
        fahrenheit = float(((celsius+32)*5/9))
        print("\nThere are about, " + str(round(fahrenheit, 1)) + " degree(s) Fahrenheit in, " + str(celsius) + " degree(s) Celsius.")
        print("Nice!")



def LitToGal(liters):
    if ( liters > 0 ):
        gallons = float((liters/3.9))
        print("\nThere are about, " + str(round(gallons, 2)) + " gallon(s) in, " + str(liter) + " liter(s).")
        print("Awesome!")



def KgToPounds(kilograms):
    if ( kilograms > 0):
         pounds = float((kilograms/0.45))
         print("\nThere are about, " + str(round(pounds, 2)) + " pound(s) in, " + str(kilogram) +  " kilogram(s).")
         print("Totally rad!")



def CmToInches(centimeters):
    if ( centimeters > 0):
        inches = float((centimeters/2.54))
        print("\nThere are about, " + str(round(inches, 2)) + " inch(es) in, " + str(centimeters) + " centimeter(s).")
        print("Alright!")



USorUK()
