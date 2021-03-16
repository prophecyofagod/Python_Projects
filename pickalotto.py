
print ("-------------------------------------------------------------------------------------------")
print ("/$$$$$$$  /$$           /$$        /$$$$$$  /$$                   /$$     /$$")
print ("| $$__  $$|__/          | $$       /$$__  $$| $$                  | $$    | $$")
print ("| $$  \ $$ /$$  /$$$$$$$| $$   /$$| $$  \ $$| $$        /$$$$$$  /$$$$$$ /$$$$$$    /$$$$$$")
print ("| $$$$$$$/| $$ /$$_____/| $$  /$$/| $$$$$$$$| $$       /$$__  $$|_  $$_/|_  $$_/   /$$__  $$")
print ("| $$____/ | $$| $$      | $$$$$$/ | $$__  $$| $$      | $$  \ $$  | $$    | $$    | $$  \ $$")
print ("| $$      | $$| $$      | $$_  $$ | $$  | $$| $$      | $$  | $$  | $$ /$$| $$ /$$| $$  | $$")
print ("| $$      | $$|  $$$$$$$| $$ \  $$| $$  | $$| $$$$$$$$|  $$$$$$/  |  $$$$/|  $$$$/|  $$$$$$/")
print ("|__/      |__/ \_______/|__/  \__/|__/  |__/|________/ \______/    \___/   \___/   \______/")
print ("--------------------------------------------------------------------------------------------")


from datetime import datetime
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

import random

def workerFunction():
    while True:
        try: x=input( '\nSelect an option:\n\n'
                      'Press 1 + Enter for Mega Millions picks\n'
                      'Q + Enter to quit \n\n'  )

        except EOFError: pass
        if x.lower().startswith('q'):
            print("Done! Thanks for playing.")
            break

        if x == '1': print( '\nMega Millions',factory.factoryLogic( 1, 75, 5 ),factory.factoryLogic( 1, 15, 1 ) )



class factory:

    def __init__( self ): self.a = 0


    def factoryLogic( startPosi, endPosi, interateNumber ):
        a = random.sample( range( startPosi, endPosi+1 ), interateNumber )
        a.sort()
        return a

    def repeater( times, f, functionArgs ):
        return_list = []
        for i in range( times ): return_list.append( f( functionArgs[0], functionArgs[1], functionArgs[2]  ) )
        return return_list


if __name__ == '__main__':
	workerFunction()
