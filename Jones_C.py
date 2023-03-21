#This program allows the user to create and maintain a simple database of students. Users have the option to add and remove students, assign grades to
#students in the database, and also list the current database.
#The data structure being used to acheive this is the 'list' structure.

def inputStudentName():
    #This method will prompt the user to enter a student name containing atleast 3 characters with one of them being a space and will only return the string once the criteria is met.
    student = input("Please enter student name [FIRST NAME] [SPACE] [SURNAME]: ")
    while len(student) < 3 or ' ' not in student:
        print("Please enter both first and last name seperated by one space")
        print('')
        student = input("Please enter student name [FIRST NAME] [SPACE] [SURNAME]: ")
    return student

def inputGrade():
    #This method will prompt the user to enter a grade that is used in the grading scheme, and will only return the string once the grade matches one of the appropriate grades found in the grading scheme.
    gradeScheme = ['A','B','C','D']
    grade = input("Please enter a grade (A,B,C or D): ")
    while grade not in gradeScheme:
        print("Invalid grade!")
        print('')
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
        print("Student already exists.")

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

    for list in gradeLists:
        if list[0] == studentToGrade:
            gradeToAdd = inputGrade()
            list.append(gradeToAdd)
            print("Grade added to " + studentToGrade + "'s record.")
            studentExists = True

    if studentExists == False:
        print("Erorr, student " + studentToGrade + " does not exist.")

def getGPA(gradeList):
    #This method will find the GPA of a given list of grades, by tallying up the total of the grade points and dividing by the number of grades assigned to the list.
    gradePoints = 0
    totalGrades = 0
    if len(gradeList) == 0:
        return None
    for grade in gradeList:
        totalGrades += 1
        if grade == 'A':
            gradePoints += 4.0
        elif grade == 'B':
            gradePoints += 3.0
        elif grade == 'C':
            gradePoints += 2.0
        elif grade == 'D':
            gradePoints += 1.0
    return round(gradePoints / totalGrades, 2)

def sortListAlphabetically(listToSort):
    #This method will loop through the strings in a list and return a new list with the strings sorted in alphabetical order.
    alphabeticalList = []

    for entry in listToSort:
        #Retrieves the last name of each student to compare
        surname = entry[entry.find(' ')+1: len(entry)]

        index = 0
        characterIndex = 0
        entryInserted = False

        while entryInserted == False:
            #If the index has reached the end of the list, the entry is added to the end of the list.
            if(index >= len(alphabeticalList)):
                alphabeticalList.insert(index, entry)
                entryInserted = True
            #If the current entry's first letter comes before the currently indexed alphabetical entry, the current entry is inserted before the currently indexed alphabetical entry in the list.
            elif surname[0] < alphabeticalList[index][0]:
                alphabeticalList.insert(index, entry)
                entryInserted = True
            #If the first letter of the current entry matches the currently indexed alphabetical entry, then the characterIndex variable is used to index through the string itself to ensure the list is completely alphebatized.
            elif surname[0] == alphabeticalList[index][0]:
                if surname[characterIndex] == alphabeticalList[index][characterIndex]:
                    characterIndex += 1
                    if characterIndex >= len(surname):
                        if(len(surname) > len(alphabeticalList[index])):
                           alphabeticalList.insert(index+1, entry) 
                        else:
                            alphabeticalList.insert(index, entry)
                        entryInserted = True
                elif surname[characterIndex] < alphabeticalList[index][characterIndex]:
                    alphabeticalList.insert(index, entry)
                    entryInserted = True
                else:
                    index+= 1
            else:
                index += 1
                
    return alphabeticalList


def listDatabase():
    #This method will loop through the student list and print each entry on a seperate line, if the list is empty it will print a simple error message.
    #It will also compare each student name to the first element of each student grade list to retreive the relevant grade list and print out the student's grades and their GPA.
    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    
    for entry in sortListAlphabetically(studentDatabase):

        stringToPrint = entry
        for gradeList in gradeLists:
            if entry == gradeList[0]:
                stringToPrint = stringToPrint + " - " + str(gradeList[1:len(gradeList)]) + "; GPA: " + str(getGPA(gradeList[1:len(gradeList)]))
        print(stringToPrint)

    
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