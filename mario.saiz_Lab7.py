#Author: Mario Saiz
#Class: COSC 1336
#Program: Lab 7 with extra credit
#Opens files, checks them against the key, states whether they passed or not,
#tells them how many they got right and wrong, then says the numbers they got wrong.
#There is also one where the person inputs answers manually, saves into a file, and then does all of the above.



def readstudentA(path):
    with open('studentA.txt', 'r') as infileA:
        contents = infileA.read()


    return contents.split('\n') 

def passfailA(answers, studentA):
    correct_list = []
    wrong_list = []


    for index, (x, y) in enumerate(zip(answers, studentA)):

        problem_number = index + 1 

        if x == y:
            correct_list.append(problem_number)
        else:
            wrong_list.append(problem_number)
            mytuple = tuple(wrong_list)


    print("________________________________________")
    print("\nStudent A: \n")
    print(len(correct_list), 'were answered correctly')
    print(len(wrong_list), 'questions were missed')

    if len(correct_list) >= 15:
        print('\nCongrats, you have passed!')
    else:
        print("\nYou failed.")


    print ('\nYou missed question numbers: ' + str(mytuple)[1:-1])




def readstudentB(path):
    with open('studentB.txt', 'r') as infileB:
        contents = infileB.read()


    return contents.split('\n') 


def passfailB(answers, studentB):
    correct_list = []
    wrong_list = []


    for index, (x, y) in enumerate(zip(answers, studentB)):

        problem_number = index + 1 

        if x == y:
            correct_list.append(problem_number)
        else:
            wrong_list.append(problem_number)
            mytuple = tuple(wrong_list)


    print("________________________________________")
    print("\nStudent B: \n")
    print(len(correct_list), 'were answered correctly')
    print(len(wrong_list), 'questions were missed')

    if len(correct_list) >= 15:
        print('\nCongrats, you have passed!')
    else:
        print("\nYou failed.")


    print ('\nYou missed question numbers: ' + str(mytuple)[1:-1])




def readstudentC(path):

    index = 0
    infileC = open('studentC.txt', 'w')
    
    print("\n")

    while index < 20:
        index = index + 1
        print("What did you get for question ", index,"?")
        answer = input("Please enter yout answer with a letter (A,B,C, or D): " )
        answer = answer.upper()
        index = index - 1

        if answer == "A" or answer == "B" or answer =="C" or answer == "D":


            infileC.write(str(answer) + '\n')

            index = index + 1

        else:
            print("ERROR!")
            quit()

    infileC.close()



    
    with open('studentC.txt', 'r') as infileC:
        contents = infileC.read()


    return contents.split('\n') 


def passfailC(answers, studentC):
    correct_list = []
    wrong_list = []


    for index, (x, y) in enumerate(zip(answers, studentC)):

        problem_number = index

        if x == y:
            index = index + 1
            correct_list.append(index)
        else:
            problem_number = index + 1
            wrong_list.append(problem_number)
            mytuple = tuple(wrong_list)


    print("________________________________________")
    print("\nStudent C: \n")
    print(len(correct_list), 'were answered correctly')
    print(len(wrong_list), 'questions were missed')

    if len(correct_list) == 20:
        print ('\nYou got a 100, congrats!')

    elif len(correct_list) >= 15:
        print('\nCongrats, you have passed!')
        print('\nYou missed question numbers: ' + str(mytuple)[1:-1])
    
    else:
        print("\nYou failed.")
        print('\nYou missed question numbers: ' + str(mytuple)[1:-1])

def main( ): 
    key = ('A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 
        'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A')

    option = int(input("Would you like to read Student A (1), Student B (2), Student C (3), or Quit (4)?: "))


    if option == 1:
        student_answersA = readstudentA('studentA.txt')
        passfailA(key, student_answersA)
    if option == 2:
        student_answersB = readstudentB('studentB.txt')
        passfailB(key, student_answersB)
    if option == 3:
        student_answersC = readstudentC('studentC.txt')
        passfailC(key, student_answersC)
    if option == 4:
        exit()

if __name__ == '__main__':
    main()
