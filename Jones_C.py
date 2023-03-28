#This program allows the user to create and maintain a simple database of students. Users have the option to add and remove students, assign grades to
#students in the database, and also list the current database.
#The data structure being used to acheive this is the 'list' structure.
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
        print("Student " + studentToAdd + " already exists.")

def removeStudent():
    #This method will retreive the string from the inputStudentName method and remove it from a list provided the list contains an identical string.
    #It will also search for the grades list that is matched to the student the user wishes to remove, to ensure their grades are removed from the list containg the grades lists.

    #Check database contains at least 1 student, print an error message and return to menu if it does not.
    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    
    studentToRemove = inputStudentName()
    
    #Check student exists inside student list, remove the student string and grade list if they do.
    if studentToRemove in studentDatabase:
        studentDatabase.remove(studentToRemove)
        
        #Removing relevant grades list.
        for list in gradeLists:
            if list[0] == studentToRemove:
                gradeLists.remove(list)

        print("Student " + studentToRemove + " removed.")
    #If student does not exist inside student list, print and error message and return to menu.
    else:
        print("Student " + studentToRemove + " doesn't exist.")

def addGrade():
    #This method will ask for two strings, the student to grade and the grade itself. It will then search through the list containing student grade lists by checking the first entry in each of these lists to match the student name.
    #Once the list is found, the grade is then appended on to the end of the list.
    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    studentToGrade = inputStudentName() 
    studentExists = False #Initialise flag variable

    #Looping through each grade list and comparing index 0 to the student's name to ensure the grades list the grade is added to belongs the the correct student. Use flag variable to confirm student grade list exists.
    for list in gradeLists:
        if list[0] == studentToGrade:
            gradeToAdd = inputGrade()
            list.append(gradeToAdd)
            print("Grade added to " + studentToGrade + "'s record.")
            studentExists = True

    #Check the flag variable was raised, if it was not, print and error message informing the user, the student does not exist.
    if studentExists == False:
        print("Error, student " + studentToGrade + " does not exist.")

def getGPA(gradeList):
    #This method will find the GPA of a given list of grades, by tallying up the total of the grade points and dividing by the number of grades assigned to the list.
    gradePoints = 0
    totalGrades = 0

    #if the grade list passed through to this method is empty, return None.
    if len(gradeList) == 0: 
        return None
    #Add the numerical value of each grade found in the grade list
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
    
    #Divide the numerical total by the amount of grades and round it to 2dp, return this value
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

        #Loop through each student name in the sorted list to compare the current entry, increase the index var each time if the current entry makes it through the loop without being sorted.
        while entryInserted == False:
            #if there are entries in the alphabetical list to compare to, a variable is create to slice the surname out.
            if index < len(alphabeticalList):
                sortedEntrySurname = alphabeticalList[index][alphabeticalList[index].find(' ')+ 1: len(alphabeticalList[index])]
            #If the index has reached the end of the list, the entry is added to the end of the list.
            if(index >= len(alphabeticalList)):
                alphabeticalList.insert(index, entry)
                entryInserted = True
            #If the current entry's first letter comes before the sorted entry's first letter, the current entry is inserted BEFORE the sorted entry in the list.
            elif surname[0] < sortedEntrySurname[0]:
                alphabeticalList.insert(index, entry)
                entryInserted = True
            #If the first letter of the current entry matches the sorted entry, then the characterIndex variable is used to index through the string itself to ensure the list is completely alphebatized.
            elif surname[0] == sortedEntrySurname[0]:
                if surname[characterIndex] == sortedEntrySurname[characterIndex]:
                    characterIndex += 1
                    #If the character index variable has reached the end of either of the entries, the indexed entry is placed based on the length, shorter BEFORE.
                    if characterIndex >= len(surname) or characterIndex >= len(sortedEntrySurname):
                        #if current entry is longer than the sorted entry, place it AFTER.
                        if(len(surname) > len(sortedEntrySurname)): 
                           alphabeticalList.insert(index+1, entry) 
                        #If the current entry is the same length or shorter than the sorted entry, place it BEFORE.
                        else: 
                            alphabeticalList.insert(index, entry)
                        entryInserted = True
                #If the currently indexed char of the current entry comes BEFORE the currently indexed char of the sorted entry, place the curren entry BEFORE
                elif surname[characterIndex] < sortedEntrySurname[characterIndex]: 
                    alphabeticalList.insert(index, entry)
                    entryInserted = True
                else:
                    index+= 1
            #If the current entry's first letter comes AFTER the sorted entry's first letter, then increase in the index variable and loop through again.
            else:
                index += 1
                
    return alphabeticalList


def listDatabase():
    #This method will loop through the student list and print each entry on a seperate line, if the list is empty it will print a simple error message.
    #It will also compare each student name to the first element of each student grade list to retreive the relevant grade list and print out the student's grades and their GPA.
    
    #Check if student database is empty, print an error message and return to menu if so.
    if len(studentDatabase) == 0:
        print("Database empty.")
        return
    
    #Looping through an alphabetically sorted version of the student list to print the students in alphabetical order.
    for entry in sortListAlphabetically(studentDatabase):
        stringToPrint = entry #Add student name to string
        #Finding relevant grade list to print and run through the get gpa method to also return the student's gpa aswell as their grades.
        for gradeList in gradeLists:
            if entry == gradeList[0]:
                stringToPrint = stringToPrint + " - " + str(gradeList[1:len(gradeList)]) + "; GPA: " + str(f'{getGPA(gradeList[1:len(gradeList)]):.2f}') #concatenate student's grade list and gpa to string
        print(stringToPrint) #Print concatenated string

    
def main():
    programRunning = True
    print("""
Please choose from the following options.
A - Add student
R - Remove student
G - Add Grade
L - List database
X - Exit

""")
    while programRunning:
        action = input("Choose A, R, L, or G ('X' for exit): ") #Get user input
        print('')

        #Compare user's input with available options, if none match, loop will run again asking the user for another input.
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
        
studentDatabase = [] #List containg all student names within database.
gradeLists = [] #List containing multiple lists, each assigned to a student, these will store the student's grades. The first element of each will be the student's names to allow the program to retreive the correct list for each student.

main()