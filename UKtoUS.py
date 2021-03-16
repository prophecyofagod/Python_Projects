#Author: Mario Saiz
#Class: COSC 1336
#Program: Lab 5a
#Instantiate classes, and call them up, modifying assignment Lab 4a

print("\n"*20)
name = input("What is your name?: ")


def main():
    tries = 0

    print("\nAlright, "+ str(name) + ", I know you've been struggling with converting measurements, ")
    print("so I wrote a program to help you convert from the metric system to the ")
    print("imperial system. Go ahead and pick a number, ONLY 1 through 5, for which ")
    print("the measurement you want to convert to, and you'll get the answer for both.")

    print('\n(1): Kilometers to Miles? ')
    print('(2): Celcius to Fahrenheit? ')
    print('(3): Liters to Gallons? ')
    print('(4): Kilograms to Pounds? ') 
    print('(5): Centimeters to Inches? ')


    option = int(input("Please choose an option, 1 - 5: "))


    
#---------------------
    if (option == 1):
        kilometers = float(input("\nAlright, " + str(name) + ", how many Kilometers do you want converted into Miles?: "))
        while (kilometers < 0):
            if tries == 3:
                break
            print("\nValues cannot be negative.")
            print(' ')
            kilometers = float(input("\nAlright, " + str(name) + ", how many Kilometers do you want converted into miles?: "))
            tries += 1
        KmToMiles(kilometers)

#-----------------------------------------------------
    elif (option == 2):
        celcuis = float(input("\nAlright, " + str(name) + ", how many degrees Celsius do you want converted into degrees Fahrenheit?: "))
        while (celsius < -1000) or (celsius > 1000):
            if tries == 3:
                break
            print("\nValues cannot be smaller than -1000 or bigger than 1000.")
            print(' ')
            celsius = float(input("\nAlright, " + str(name) + ", how many degrees Celsius do you want converted into degrees Fahrenheit?: "))
            tries += 1
        CelToFah(celsius)

#-------------------------
    elif (option == 3):
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
    elif (option == 4):
        kilograms = float(input("\nAlright, " + str(name) +  ", how many Kilograms do you want converted into Pounds?: "))
        while ( kilograms < 0 ):
            if tries == 3:
                break
            print("\nValues cannot be 0 or a negative.")
            print(" ")
            kilograms = float(input("\nAlright, " + str(name) +  ", how many Kilograms do you want converted into Pounds?: "))
            tries += 1
        KgToPounds(kilograms)

#------------------------
    elif (option == 5):
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
        print("Error, value is not 1 - 5!")
        exit()

#-----------------------------------------------------------------------------------------------------------------------------------------------

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


main()
