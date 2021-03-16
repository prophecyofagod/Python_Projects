#Author: Mario Saiz
#Class: COSC 1336
#Program: Lab 6a
#Asks user how many powerballs they want, and then stores them into a file.


import random

def main():
    try:
        Powerball()
    except:
        print("An error has occured!")

def Powerball():
    ticket =[]
    ticketCount = int(input('How many powerball tickets would you like to buy? '))
    file = open('powerball.txt','a')

    for n in range(ticketCount):
        PB = random.randint(1,26)
        ticket = sorted(random.sample(range(1,69),5))
        a = ticket[0]
        b = ticket[1]
        c = ticket[2]
        d = ticket[3]
        e = ticket[4]
        print(str(a).zfill(2), str(b).zfill(2), str(c).zfill(2), str(d).zfill(2), str(e).zfill(2), str(PB).zfill(2))

        for item in ticket:
            file.write(str(item).zfill(2) + ' ')
        file.write(str(PB).zfill(2) + '\n')
    file.close()
    print('All records processed and written to file.')

main()
