#Author: Mario Saiz
#Class: COSC 1336
#Program: Lab 4c
#Getting grades that are entered, determining the letter grade, and
#then calculating the class average by adding all the grades up, and
#dividing by the number of entered grades

print("\n"*25)
name = input("What is your name?: ")
grade = float(input("Please enter a grade, " + str(name) + ", or a -1 to end the program: "))

totalgrades = 0
gradecount = 0

while (grade != -1):
    if (grade >= 90 and grade <= 100):
        print ("\nYou got an A! You're doing amazing!")
    elif (grade >= 80 and grade <= 89):
        print ("\nYou got a B! You're doing great, keep it up!")
    elif (grade >= 70 and grade <= 79):
        print ("\nYou got a C! You're doing okay, but you can do better.")
    elif (grade >= 60 and grade <= 69):
        print ("\nYou got a D! You're not doing so well in class. Try harder.")
    elif (grade <= 59 and grade >= 0):
        print ("\nYou got an F! You really need to get serious about class.")
    print()

    gradecount = (gradecount + 1)
    totalgrades = (totalgrades + grade)
    grade = float(input("Enter a grade or a -1 to end the program: "))
    
if (gradecount == 0):
    print("\nNo grades found, " +str(name) + ". Class average cannot be calculated.")
elif (grade == -1):
    classaverage = totalgrades/gradecount
    print("\nThe class average is a(n) " + format(classaverage, ".2f") + ", " + str(name) + ".")

