from save import *
import time

phonebook = init()

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
    phonebook_options = int(input("What would you like to do? Select 1 - 5  "))
    return phonebook_options

def previous():
    menu_restart = "Would you like to go to the previous menu? Y / N  "
    back = input(menu_restart).upper()
    return back

def choice_previous():
    if previous() == "Y":
        save(phonebook)
        print("Redirecting...")
        time.sleep(1)
    else:
        save(phonebook)
        print("Good bye!")