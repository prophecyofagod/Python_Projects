#Author: Mario Saiz
#Class: COSC 1336
#Program: Lab 5b
#Make a program that displays a makeshift lotto ticket with loops, formats, imports, and tries.



import random
from datetime import datetime

def main():
    print("\n"*25)

    print (" ********************************************************************************************************* ")
    print (" * /$$$$$$$  /$$           /$$            /$$$$$$      /$$                   /$$     /$$                 * ")
    print (" * | $$__  $$|__/          | $$           /$$__  $$    | $$                  | $$    | $$                * ")
    print (" * | $$  \ $$ /$$  /$$$$$$$| $$   /$$    | $$  \ $$    | $$        /$$$$$$  /$$$$$$ /$$$$$$    /$$$$$$   * ")
    print (" * | $$$$$$$/| $$ /$$_____/| $$  /$$/    | $$$$$$$$    | $$       /$$__  $$|_  $$_/|_  $$_/   /$$__  $$  * ")
    print (" * | $$____/ | $$| $$      | $$$$$$/     | $$__  $$    | $$      | $$  \ $$  | $$    | $$    | $$  \ $$  * ")
    print (" * | $$      | $$| $$      | $$_  $$     | $$  | $$    | $$      | $$  | $$  | $$ /$$| $$ /$$| $$  | $$  * ")
    print (" * | $$      | $$|  $$$$$$$| $$ \  $$    | $$  | $$    | $$$$$$$$|  $$$$$$/  |  $$$$/|  $$$$/|  $$$$$$/  * ")
    print (" * |__/      |__/ \_______/|__/  \__/    |__/  |__/    |________/ \______/    \___/   \___/   \______/   * ")
    print (" ********************************************************************************************************* ")



    
    print ("\n\t\t     Welcome to the automated Powerball QuickPick Provider! \
    \n\t\t        Here you may purchase up to 10 QuickPick numbers. \
    \n\t\t      QuickPicks are provided at a rate of $2.00 per play.")
    x = int(input("\n\n\t\t              Input desired number of QuickPicks: "))
    print (datetime.now().strftime('\n\n\t\t                 Printed: %Y-%m-%d %H:%M:%S'))
    print("\n")
    if (x <= 0):
        print ("\n\n\t\t\tERROR; Number of tickets cannot be equal to or less than 0.")
    elif (x > 10):
        print ("\n\n\t\t\tERROR; You cannot purchase more than 10 tickets.")
    elif (x > 0 and x <= 10):
        alpha = ['A.','B.','C.','D.','E.','F.','G.','H.','I.','J.']
        for n in range(x):
          result = powerball()
          a = result[0]
          b = result[1]
          c = result[2]
          d = result[3]
          e = result[4]
          f = result[5]

          print ("\t\t                 " + "QP " + alpha[n], format (a, '02d'), format (b, '02d'), \
                 format (c, '02d'), format (d, '02d'), \
                 format (e, '02d') +   " [PB] "+ format (f, '02d'))
        xyz = (2*x)
        print("\n\n\n\t\t                          Cost: $" + format(xyz, '.2f'))
        option = input("\n\t\t                          Again?[Y/N]: ")
        tries = 3
        while (tries > 0):
            if (option == "Y" or option == "y"):
                tries = (tries - 3)
                main()
            if (option == "N" or option == "n"):
                print ("\n\t\t     Thank you for using the Powerball QuickPick Provider!")
                tries = (tries - 4)
    else:
        print("\n\t\tERROR; Invalid input entered.")
        print("\n")



def powerball():   

    result = []   


    for i in range(5):       

        number = random.randint(1,69)       

        while (number in result):           

            number = random.randint(1,69)       

        result.append(number)   
    
    result.sort()   



    result.append(random.randint(1,26))   

    return result
    return i

result = powerball()    



        
main()

    





