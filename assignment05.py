# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# MQuintana,5.17.2023,Created started script
# <Miguel Quintana>,<05.17.23>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
#objFile = None  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
strFile = "ToDo.txt"
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Item": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow["Item"] + ", " + dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strItem = str(input("What is the Item?: ")).strip()
        strPriority = str(input("What is the Priority?: ")).strip()
        dicRow = {"Item": strItem, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current Data in the Table: ")
        for dicRow in lstTable:
            print(dicRow)

        print("Current items in ToDo file: ")
        for row in lstTable:
            print(row["Item"] + "(" + row["Priority"] + ")")

        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strKeyToRemove = input("Which Item would you like to remove?: ")
        blnItemRemoved = False
        intRowNumber = 0
        while (intRowNumber < len(lstTable)):
            if(strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])):
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
        if (blnItemRemoved == True):
            print("the Item was removed ")
        else:
            print("I'm sorry i couldn't find that Item")

        print("Current items in ToDo file: ")
        for row in lstTable:
            print(row["Item"] + "(" + row["Priority"] + ")")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Current items in ToDo file: ")
        for row in lstTable:
            print(row["Item"] + "(" + row["Priority"] + ")")

        if("y" == str(input("save this data to a file y/n: ")).strip().lower()):
            objFile = open(strFile, 'w')
            for dicRow in lstTable:
                objFile.write(dicRow["Item"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved, press the [Enter] key to return to the menu")
        else:
            print("data was not saved, but previous data still existing, press [Enter] to return to the menu")

        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):

        break  # and Exit the program
