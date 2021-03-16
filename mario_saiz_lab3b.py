# Author: Mario Saiz
# Class: COSC 1336
# Program: Lab 3 Part B
# This program creates a payroll manager, stating bonuses, commission, salary, and vacation day deductions.

#This section asks for the employee's info o different topics
print("\n"*50)
name = input("Please enter your name: ")
months = int(input("\nAlright, " + str(name) + ", please the amount of years in months that you've worked in this company: "))
sales = float(input("\nNow, "+ str(name) + ", please enter your sales amount: "))
if (sales < 0):
    sales = float(input("\nError! Sales amount cannot be nagative."))

vac = int(input("\n"+str(name)+ ", how many vacations days have you taken off?: "))

#This section calculates if the employee receives a deduction or not
if (vac > 3):
    subtract = -200
else:
    subtract = 0

#This section shows the base salary
salary = float(2000)

#This section calculates the employee's commission, rate, and bonus
if (sales < 10000):
    commission = 0
    bonus = 0
    addedbonus = 0
elif (sales >= 10000) and (sales <= 100000):
    commission = (sales * .02)
    bonus = 0
    addedbonus = 0
elif (sales > 100000) and (sales <= 500000):
    commission = (sales * .15)
    if (months >= 60) and (months >= 3):
        addedbonus = 1000
        bonus = 1000
    else:
        addedbonus = 0
        bonus = 0
elif (sales > 500000) and (sales <= 1000000):
    commission = (sales * .28)
    if (months >= 3):
        bonus = 5000
    else:
        bonus = 0
    if (months >= 60):
        addedbonus = 1000
    else:
        addedbonus = 0
elif (sales > 1000000):
    commission = (sales * .35)
    if (months >= 3):
        bonus = 100000
    else:
        bonus = 0
    if (months >= 60):
        addedbonus = 1000
    else:
        addedbonus = 0

#This section turns the years into months
yr1 = (months)
yr2 = (months / 12)
monthsxtra = (yr1 % 12)

#Net pay calculation
netsalary = (salary + commission + bonus + subtract + addedbonus)

#Output
print ("Employee: ", name)
print ("Time with the company: ", int(yr2),"year(s), and", int(monthsxtra),"month(s).")
print ("----------------------------------------------")
print ("Base Salary".ljust(20),             "|".ljust(3),           "$".ljust(10),              (str(format(salary, ',.2f'))).rjust(10))
print ("Commission".ljust(20),              "|".ljust(3),           "$".ljust(10),              (str(format(commission,",.2f"))).rjust(10))
print ("Bonus".ljust(20),                   "|".ljust(3),           "$".ljust(10),              (str(format(bonus,",.2f"))).rjust(10))
print ("Additional Bonus".ljust(20),        "|".ljust(3),           "$".ljust(10),              (str(format(addedbonus,",.2f"))).rjust(10))
print ("Deductions".ljust(20),              "|".ljust(3),           "$".ljust(10),              (str(format(subtract,",.2f"))).rjust(10))
print ("Gross Pay".ljust(20),               "|".ljust(3),           "$".ljust(10),              (str(format(netsalary,",.2f"))).rjust(10))
