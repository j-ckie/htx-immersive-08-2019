import time
import save

def user_prompt():
    int(input("What would you like to do? Select 1 - 5  "))

def selection():
    menu()
    return user_prompt()

def menu():
    print("Welcome to the Electronic Phone Book")
    print("=====================")
    time.sleep(.5)
    print("Please select from one of the following:  ")
    time.sleep(1)
    print("1. Look up an entry")
    time.sleep(.3)
    print("2. Set an entry")
    time.sleep(.3)
    print("3. Delete an entry")
    time.sleep(.3)
    print("4. List all entries")
    time.sleep(.3)
    print("5. Quit")
    time.sleep(.3)
    user_prompt()

def back(phonebook):
    menu_restart = "Would you like to go to the previous menu? (Y / N)  "

    app_restart = input(menu_restart).upper()
    if app_restart == "Y":
        print("Redirecting...")
        time.sleep(1)
        menu()
    else:
        print("Good bye!")
        save.save(phonebook)

