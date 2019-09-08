# save changes to file
import time
from picklefunk import *
import os

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
    menu_options = input("What would you like to do? Select 1 - 5  ")
    return menu_options

def back(phonebook): # REMEMBER THE PARANTHESES AT THE END OF .UPPER() THIS WILL BREAK WITHOUT IT
    previous = input("Would you like to return to the previous menu? Y/N  ").upper()
    if previous == "Y":
        print("Redirecting...")
        time.sleep(.5)
        os.system('clear||cls')
        return 1
    else:
        save(phonebook)
        print("Good bye!")
        time.sleep(1)
        os.system('clear||cls')
        quit()

