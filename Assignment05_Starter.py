# ------------------------------------------------------------------------ #
# Title: Assignment05_Starter.py
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KODonnell, 8.8.2020, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = ""   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

try:
    objFile = open("ToDoList.txt", "r")
    for row in objFile:
        strData = row.split(",")
        dicRow = {"Task":strData[0], "Priority": strData[1].strip()}
        lstTable.append(dicRow)
    objFile.close()

except:
    pass

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
print("""\n\tWelcome to ToDoList!!
Select an option from the menu to get started!""")
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if lstTable == []:
            print("Your To Do list is currently empty.")
        else:
            print("\n\t<<<Current To Do List>>>\n")
            count = 0
            for row in lstTable:
                count +=1
                print(str(count)+". "+ row["Task"].capitalize() + " | " + row["Priority"].upper())
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        lstTask = str(input("Please enter a new To Do task:\n "))
        lstPriority = str(input("Please enter the priority for {} (High, Medium or Low):\n ".format(lstTask)))
        dicRow = {"Task": lstTask, "Priority": lstPriority}
        lstTable.append(dicRow)
        print("{} saved to your list!".format(lstTask).capitalize())
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strItem = str(input("Which item would you like to remove?\n "))
        count = 0
        for row in lstTable:
            if row["Task"].lower() == strItem.lower():
                lstTable.remove(row)
                count +=1
        if count > 0: print("{} has been removed.".format(strItem))
        else: print("Item not found")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["Task"].capitalize() + ", " + row["Priority"].upper()+"\n")
        print("Data Saved to File!")
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Goodbye!\n")
        break  # and Exit the program

    else:
        print("Please select an option from the menu.")
        continue