# Author: Mario Saiz
# Class: COSC 1336
# Program: Lab 6C
# Lets user input how many tickets they want, prints it out, says if there's a winner, and says how long it took to locate that line.

import random

tickets =[]
print("***Texas Powerball Number Generator***")
ticketCount = int(input('How many tickets do you want?: '))
print("\nSearching.....")
file = open('powerball.txt','w')
def Powerball():
    try:
        

        for n in range(ticketCount):
            PB = random.randint(1,26)
            ticket = sorted(random.sample(range(1,69),5))
            a = ticket[0]
            b = ticket[1]
            c = ticket[2]
            d = ticket[3]
            e = ticket[4]

            for item in ticket:
                file.write(str(item).zfill(2) + ' ')
            file.write(str(PB).zfill(2) + '\n')
            stringx = ()
            stringx = stringx + (str(a).zfill(2), str(b).zfill(2), str(c).zfill(2), str(d).zfill(2), str(e).zfill(2), str(PB).zfill(2))
            
        mystring = ' '.join(map(str, (stringx)))
        
        file.close()
        print("FOUND!\n")
        print(mystring)

        List = open('powerball.txt','r')
        data = List.read()
        
        if mystring in data:
            print("\nYou are a winner!")
        else:
            print("\nSorry, you didn't win.")
        
    except IOError:
        print('404 File not found')
    except IndexError:
        print('Indexing error')
    except:
        print('An error occurred')


import time
start_time = time.time()
Powerball()
time =(time.time() - start_time)
print("\nThis is how many seconds it took to find the winner: " + format(time,'.2f') + " seconds")



