#This program allows the user to create and maintain a simple database of students. Users have the option to add and remove students, and also list the current database.
#The data structure being used to acheive this is the 'list' structure.
#Users are prompted to enter and string containing a student name which is then either appended to or removed from a list.
#
#The main loop will ask the user to enter a string to pick from the available options.
#If the user picks a valid option, they will run through the method until it is complete after which they will 
#be returned to the main loop to repeat the process.
#Should the user enter an invalid string, they will simply be prompted for the string again.
#Should the user pick the 'Exit' option, the main loop will be terminated, a goodbye messgae printed and the program will end.

def inputStudentName():
    #This method will prompt the user to enter a student name containing atleast 3 characters with one of them being a space and will only return the string once the criteria is met.
    student = input("Please enter student name [FIRST NAME] [SPACE] [SURNAME]: ")
    while len(student) < 3 or ' ' not in student:
        print("Please enter both first and last name seperated by one space")
        student = input("Please enter student name [FIRST NAME] [SPACE] [SURNAME]: ")
    return student

def inputGrade():
    #This method will prompt the user to enter a grade that is used in the grading scheme, and will only return the string once the grade matches one of the appropriate grades found in the grading scheme.
    gradeScheme = ['A','B','C','D']
    grade = input("Please enter a grade (A,B,C or D): ")
    while grade not in gradeScheme:
        print("Invalid grade!")
        grade = input("Please enter a grade (A,B,C or D): ")
    return grade

def addStudent():
    #This method will retreive the string from the inputStudentName method and append it to a list provided the list does not contain an identical string.
    #It will also generate a new list that will store all grades for the new student. This list is added to another list containg all the grade lists.
    studentToAdd = inputStudentName()
    if studentToAdd not in studentDatabase:
        studentDatabase.append(studentToAdd)
        
        #Generating new grades list.
        newGradesList = [studentToAdd]
        gradeLists.append(newGradesList)

        print("Student " + studentToAdd +" added.")
    else:
        print("Student " + studentToAdd + " already exists.")

def removeStudent():
    #This method will retreive the string from the inputStudentName method and remove it from a list provided the list contains an identical string.
    #It will also search for the grades list that is matched to the student the user wishes to remove, to ensure their grades are removed from the list containg the grades lists.

    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    studentToRemove = inputStudentName()
    if studentToRemove in studentDatabase:
        studentDatabase.remove(studentToRemove)
        
        #Removing relevant grades list.
        for list in gradeLists:
            if list[0] == studentToRemove:
                gradeLists.remove(list)

        print("Student " + studentToRemove + " removed.")
    else:
        print("Student " + studentToRemove + " doesn't exist.")

def addGrade():
    #This method will ask for two strings, the student to grade and the grade itself. It will then search through the list containing student grade lists by checking the first entry in each of these lists to match the student name.
    #Once the list is found, the grade is then appended on to the end of the list.
    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    
    studentToGrade = inputStudentName()
    studentExists = False

    #Looping through each grade list and comparing index 0 to the student's name to ensure the grades list the grade is added to belongs the the correct student.
    for list in gradeLists:
        if list[0] == studentToGrade:
            gradeToAdd = inputGrade()
            list.append(gradeToAdd)
            print("Grade added to " + studentToGrade + "'s record.")
            studentExists = True
            
    if studentExists == False:
        print("Erorr, student " + studentToGrade + " does not exist.")

def listDatabase():
    #This method will loop through a list and print each entry on a seperate line, if the list is empty it will print a simple error message.
    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    for entry in studentDatabase:
        print(entry)
    
def main():
    programRunning = True
    print("""
Please choose from the following options.
A - Add student
R - Remove student
G - add Grade
L - List database
X - Exit

""")
    while programRunning:
        action = input("Choose A, R, L, or G ('X' for exit): ")
        print('')
    
        if action == 'A':
            addStudent()
            print('')
        elif action == 'R':
            removeStudent()
            print('')
        elif action == 'G':
            addGrade()
            print('')
        elif action == 'L':
            listDatabase()
            print('')
        elif action == 'X':
            print("Thank you - Goodbye.")
            programRunning = False
        
studentDatabase = []
gradeLists = []

main()