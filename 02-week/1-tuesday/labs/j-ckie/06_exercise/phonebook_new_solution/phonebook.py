# $ python phonebook.py 
# Electronic Phone Book 
# ===================== 
# 1. Look up an entry 
# 2. Set an entry 
# 3. Delete an entry 
# 4. List all entries 
# 5. Quit
# What do you want to do (1-5)?

# If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
# If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
# If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
# If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
# If they choose to quit, end the program.

from save import *
import time
from menu import *

phonebook = init() # initializes data file -> checks if data.pickle already exists, if not, creates new data.pickle

menu_options = menu()

def main():
    init()
    if menu_options == 1:
        # print("test")
        name_lookup = input("Enter the name of the person:  ").upper()
        if name_lookup in phonebook:
            print("This person's number is:  ", phonebook[name_lookup])
            time.sleep(.2)
            choice_previous()
            main()
    
    elif menu_options == 2:
        print("Please fill in the information below:")
        new_name = input("Name:  ").capitalize()
        new_num = input("Number:  ")
        phonebook.update({new_name : new_num})
        time.sleep(.2)
        print(f"Entry stored for {new_name}")
        choice_previous()
        main()

    
    elif menu_options == 4:
        for key,val in phonebook.items():
            print("Found entry for " + key + ": " + val)
            time.sleep(.2)
        choice_previous()
        main()

    elif menu_options == 5:
        print("Good bye!")
        save(phonebook)
    else:
        print("Please choose a valid option")
        main()

main()

