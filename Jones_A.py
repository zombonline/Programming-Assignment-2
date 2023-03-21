#This program allows the user to create and maintain a simple database of students. Users have the option to add and remove students, and also list the current database.
#The data structure being used to acheive this is the 'list' structure.
#Users are prompted to enter and string containing a student name which is then either appended to or removed from a list.


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
        print("Student already exists.")

def removeStudent():
    #This method will retreive the string from the inputStudentName method and remove it from a list provided the list contains an identical string.
    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    studentToRemove = inputStudentName()
    if studentToRemove in studentDatabase:
        studentDatabase.remove(studentToRemove)
        print("Student " + studentToRemove + " removed.")
    else:
        print("Student doesn't exist.")

def listDatabase():
    #This method will loop through a list and print each entry on a seperate line, if the list is empty it will print a simple error message.
    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    for entry in studentDatabase:
        print(entry)

def main():
    programRunning = True

    while programRunning:
        action = input(
        """
Please choose from the following options.
A - Add student
R - Remove student
L - List database
X - Exit

""")
        print('')
    
        if action == 'A':
            addStudent()
        elif action == 'R':
            removeStudent()
        elif action == 'L':
            listDatabase()
        elif action == 'X':
            print("Thank you - Goodbye.")
            programRunning = False
        
studentDatabase = []
main()