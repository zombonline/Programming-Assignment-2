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

def addStudent():
    #This method will retreive the string from the inputStudentName method and append it to a list provided the list does not contain an identical string.
    studentToAdd = inputStudentName()
    if studentToAdd not in studentDatabase:
        studentDatabase.append(studentToAdd)
        print("Student " + studentToAdd +" added.")
    else:
        print("Student " + studentToAdd + " already exists.")

def removeStudent():
    #This method will retreive the string from the inputStudentName method and remove it from a list provided the list contains an identical string.

    #Check database contains at least 1 student, print an error message and return to menu if it does not.
    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    
    studentToRemove = inputStudentName()

    #Check student exists inside student list, remove the student string if they do.
    if studentToRemove in studentDatabase:
        studentDatabase.remove(studentToRemove)
        print("Student " + studentToRemove + " removed.")
    #If student does not exist inside student list, print and error message and return to menu.
    else:
        print("Student " + studentToRemove + " doesn't exist.")

def listDatabase():
    #This method will loop through a list and print each entry on a seperate line, if the list is empty it will print a simple error message.
    
    #Check if student database is empty, print an error message and return to menu if so.
    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    #If database is not empty, loop through and print each student's name.
    for entry in studentDatabase:
        print(entry)

def main():
    programRunning = True
    print("""
Please choose from the following options.
A - Add student
R - Remove student
L - List database
X - Exit

""")
    while programRunning:
        action = input("Choose A, R, or L ('X' for exit): ") #Get user input
        print('')

        #Compare user's input with available options, if none match, loop will run again asking the user for another input.
        if action == 'A':
            addStudent()
            print('')
        elif action == 'R':
            removeStudent()
            print('')
        elif action == 'L':
            listDatabase()
            print('')
        elif action == 'X':
            print("Thank you - Goodbye.")
            programRunning = False
        
studentDatabase = [] #List containg all student names within database.

main()