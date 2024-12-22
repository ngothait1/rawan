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

def saveNewEntry():
    global total_age, num_users
    
    id = input("ID: ") 
    
    while id.isdigit():
        id_exists = False
        for user in users_list:
            if user["ID"] == int(id):
                id_exists = True
                break
        
        if id_exists:
            print("ERROR: ID already exists.")
            pressEnter()
            return
        else:
            name = input("Name: ")
            age = input("Age: ")
            if age.isdigit():
                age = int(age)
                user_dict = {"ID": int(id), "Name": name, "Age": age}
                users_list.append(user_dict)
                
                total_age += age
                num_users += 1
                
                print("ID " + id + " saved successfully")
                pressEnter()
                return
            else:
                print("ERROR: Age must be a number.")
                pressEnter()
                return
    
    print("ERROR: ID must be a number. " + id + " is not a number")
    pressEnter()


def printAgesAvg():
    if num_users > 0:
        print(total_age / num_users)
        pressEnter()
    else:
        print("No users.")
        pressEnter()


def searchById(users_list):
    search_id = input("Please enter the ID you want to look for: ")
    
    if not search_id.isdigit():
        print("ERROR: ID must be a number.")
        pressEnter()
        return
    
    search_id = int(search_id)
    
    for user in users_list:
        if user["ID"] == search_id:
            print("Name: " + user['Name'])
            print("Age: " + str(user['Age']))
            print("ID: " + str(search_id))
            pressEnter()
            return
            
    
    print("ERROR: ID " + str(search_id) + " is not saved.")
    pressEnter()

def printAllNames(users_list):
    if len(users_list) > 0:
        for user in users_list:
            print(user["Name"])
    else:
        print("No users available.")
    pressEnter()


def printAllIds(users_list):
    if len(users_list) > 0:
        for user in users_list:
            print(user["ID"])
    else:
        print("No users available.")
    pressEnter()

def printAllEntries(users_list):
    if len(users_list) > 0:
        for user in users_list:
            print(user)
    else:
        print("No users available.")
    pressEnter()

def printEntryByIndex(user_list):
    search_index = input("Please enter the index of the entry want to print: ")
    
    if not search_index.isdigit():
        print("ERROR: index must be a number. " + search_index + "is not a number")
        pressEnter()
        return
    
    search_index = int(search_index)
    if search_index < 0 or search_index >= len(user_list):
        print("ERROR: Index out of range. The maximum index allowed is: " + str(len(user_list)-1))
        pressEnter()
        return
    print(user_list[search_index])
    pressEnter()
    
    
users_list = []
total_age = 0
num_users = 0
while True:
    
    choice = printMenu()

    if choice == '1':
        saveNewEntry()
    elif choice == '2':
        searchById(users_list)
    elif choice == '3':
        printAgesAvg()
    elif choice == '4':
        printAllNames(users_list)
    elif choice == '5':
        printAllIds(users_list)
    elif choice == '6':
        printAllEntries(users_list)
    elif choice == '7':
        printEntryByIndex(users_list)
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
