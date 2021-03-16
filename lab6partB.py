#Author: Mario Saiz
#Class: COSC 1336
#Program: Lab 6b
#Prints out every line from the file and tells you how many inputs there are.

def main ():
  
  counter=0
  infile = open ('powerball.txt', 'r')

  number = infile.readline()
  number = number.rstrip('\n')

  while number != '':
      print (number)  
      number = infile.readline()
      number = number.rstrip('\n')
      counter = counter +1

  infile.close()
  print ("Number of Powerball numbers Generated = ", counter)

main ()
