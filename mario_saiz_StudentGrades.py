# Mario Saiz

def main():
    another_student = "y"
    student = 0

    while another_student == "y" or another_student == "Y":
        print()
        student = student + 1
        total = 0
        
        student_name = input("Enter student's name: " )
        number_of_grades = int(input("\nPlease enter number of grades: "))
        gradecount = 0
        totalgrade = 0
        

        for grade_num in range(number_of_grades):
            print("grade number",grade_num + 1, end="")
            score = float(input(' : '))
            total = total + score

        avg = total / number_of_grades
        list = avg
        grade = letter_grade(avg)
        

        print(student_name,"'s Average is: ", avg, " and his/her grade is: ", grade)
        print ()


        totalgrades = totalgrades + grade
        gradecount = gradecount + 1
        another_student = input("Do you have another student to enter? Type (-1) to quit. ")
             
    while another_student == -1:
        
        print ()
        classavg = totalgrades/gradecount
        print("The class average is " + format(classavg, ".2f") + " and you entered ",student," students grades.")
        exit()
        


def letter_grade(avg):
    if avg >= 90:
        return "You're doing amazing, you have an A."
    elif avg >= 80:
        return "You're doing awesome, you have an B."
    elif avg >= 70:
        return "You're doing o.k., you have an C."
    elif avg >= 60:
        return "You're not doing so great, you have an D."
    elif avg <= 59:
        return "You need to start getting serious, you have an F."

main()
