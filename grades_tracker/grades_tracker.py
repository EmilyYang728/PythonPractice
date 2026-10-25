grades = []

print("Add your grades! (betweeb 0-100) Type 'done' when finished ")

enteringGrades = True

while enteringGrades == True:
    
    addingGrade = input("add a grade: ")

    if addingGrade.lower() == "done":
        print("you've finished inputting grades.")
        break
    try:
        addingGrade = float(addingGrade)
    except ValueError:
        print("you must enter a number or 'done'")
        continue
    if 0 <= addingGrade <= 100:    
        grades.append(float(addingGrade))
    else:
        print("grade too high or too low")

calculating = True

while calculating == True:

    userInput = input("what would you like to do? ")

    if userInput.lower() == "average":
        total = 0
        average = 0
        if len(grades) > 0:
            for x in grades:
                total += x
            average = total / len(grades)
            print("the average is: ", average)
            

    elif userInput.lower() == "remove grade":
        removedGrade = float(input("which grade would you like to remove? "))
        if removedGrade in grades:
            grades.remove(removedGrade)
            print("here is the new list: ", grades)
        else:
            print("the grade is not in the list")

    elif userInput.lower() == "add grade":
        addedGrade = float(input("what grade would you like to add? "))
        try:
            addedGrade = float(addedGrade)
        except ValueError:
            print("you must enter a number")
            continue
        grades.append(addedGrade)
        print("here is the new list ", grades)
        
    elif userInput.lower() == "length":
        print("the length is: ", len(grades))

    elif userInput.lower() == "stop":
        print("you are stopping the code")
        break

    else:
        print("oop typo? ")
