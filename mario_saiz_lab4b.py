#Author: Mario Saiz
#Class: COSC 1336
#Program: Lab 4b
#Creating a right triangle which is upside down and a regular triangle, plus other samples.

import time

print("\n" *25)
name = input("Hello there, tell me your name!: ")
time.sleep(0.25)
print("\nHere are your triangles, " + name + ".")

n = 0

print ("\nPattern A:")
for x in range (0,11):
    n = n + 1
    for a in range (0, n-1):
        time.sleep(0.02)
        print ('*', end = '')
    time.sleep(0.02)
    print()
print ('')
print ("Pattern B:")
for b in range (0,11):
    n = n - 1
    for d in range (0, n+1):
        time.sleep(0.02)
        print ('*', end = '')
    print()
print ('')

print ("Pattern C:")
for e in range (11,0,-1):
    time.sleep(0.02)
    print((11-e) * ' ' + e * '*')

print ('')
print ("Pattern D:")
for g in range (11,0,-1):
    time.sleep(0.02)
    print(g * ' ' + (11-g) * '*')

print ('')
print ("Pattern E:")
n = 13                                                                          
for i in range(13,0,-2):                                                            
    numwhite = ((n-i)/2) +1
    nw = int(numwhite)
    time.sleep(0.02)
    print (" "*nw + '*'*i)
