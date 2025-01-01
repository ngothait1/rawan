def pressEnter():
    input("Press Enter to continue")
    

def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID ")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")
    num = input("Please enter your choice: ")
    return num

def getNumber():
    while True:
        user_input = input("ID: ")
        if user_input.isdigit():  
            return int(user_input)  
        else:
            print("ERROR: ID must be a number. " + str(id) + " is not a number")
            

def saveNewEntry(users_list, users_dict, total_age):
    id = getNumber()
    if id in users_list:
            print("ERROR: ID already exists.")
            return total_age
    else:
        name = input("Name: ")
        age = input("Age: ")
        if age.isdigit():
            age = int(age)
            users_dict[id]= {"Name": name, "Age": age}
            users_list.append(id)
            total_age += age
            print("ID " + str(id) + " saved successfully")
            return total_age
        else:
            print("ERROR: Age must be a number.")
            return total_age
   


def printAgesAvg(total_age,users_dict):
    if len(users_dict) > 0:
        print(total_age / len(users_dict))
    else:
        print("No users.")


def printUsersDetails(users_dict, id):
    print("Name: " + users_dict['Name'])
    print("Age: " + str(users_dict['Age']))
    print("ID: " + str(id))

def searchById(users_list, users_dict):
    search_id = input("Please enter the ID you want to look for: ")
    if not search_id.isdigit():
        print("ERROR: ID must be a number.")
        return 
    search_id = int(search_id)
    if search_id in users_list:
        printUsersDetails(users_dict[search_id], search_id)
    else:
        print("ID " + str(search_id) + " is not saved")
        return

       
def printAllNames(users_dict):
    if len(users_dict) > 0:
        for user in users_list:
            print(user["Name"])
    else:
        print("No users available.")

def printAllIds(users_list):
    if len(users_list) > 0:
        for user in users_list:
            print(user["ID"])
    else:
        print("No users available.")

def printAllEntries(users_list):
    if len(users_list) > 0:
        for user in users_list:
            printUsersDetails(users_dict[user], user)
    else:
        print("No users available.")

def printEntryByIndex(user_list, users_dict):
    search_index = input("Please enter the index of the entry want to print: ")
    user_id = user_list[int(search_index)]
    if not search_index.isdigit():
        print("ERROR: index must be a number. " + search_index + "is not a number")
        return
    
    search_index = int(search_index)
    if search_index < 0 or search_index >= len(user_list):
        print("ERROR: Index out of range. The maximum index allowed is: " + str(len(user_list)-1))
        return
    printUsersDetails(users_dict[user_id], user_id)
    
    
users_list = []
users_dict = {}
total_age = 0
num_users = 0
while True:
    
    choice = printMenu()

    if choice == '1':
        total_age = saveNewEntry(users_list, users_dict, total_age)
    elif choice == '2':
        searchById(users_list, users_dict)
    elif choice == '3':
        printAgesAvg(total_age, num_users)
    elif choice == '4':
        printAllNames(users_list)
    elif choice == '5':
        printAllIds(users_list)
    elif choice == '6':
        printAllEntries(users_list)
    elif choice == '7':
        printEntryByIndex(users_list, users_dict)
    elif choice == '8':
        while True:
            confirm_exit = input("Are you sure you want to exit?(y/n): ")
           
            if confirm_exit == 'y':
                print("Goodbye!")
                exit()
            elif confirm_exit == 'n':
                break 
           
    else:
        print("Option " + choice + " does not exist. Please try again.")
    pressEnter()
