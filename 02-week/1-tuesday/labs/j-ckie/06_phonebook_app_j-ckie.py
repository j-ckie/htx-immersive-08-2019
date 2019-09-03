# You will write a command line program to manage a phone book. When you start the phonebook.py program, it will print out a menu and ask the user to enter a choice:

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

import time

phonebook = [
    {"name" : "Melissa", "number" : "555-554-5523"},
    {"name" : "Jared", "number" : "555-987-2350"},
    {"name" : "Angela", "number" : "555-872-9410"}
]

def main():

    print("Welcome to the Electronic Phone Book")
    print("=====================")
    time.sleep(1)
    print("Please select from one of the following:  ")
    time.sleep(1)
    print("1. Look up an entry")
    time.sleep(.5)
    print("2. Set an entry")
    time.sleep(.5)
    print("3. Delete an entry")
    time.sleep(.5)
    print("4. List all entries")
    time.sleep(.5)
    print("5. Quit")
    time.sleep(.5)
    phonebook_options = input("What would you like to do? Select 1 - 5  ")

    if phonebook_options == "1": # REMEMBER TO PUT INPUT IN QUOTES!!!!
        name_lookup = input("Enter the name of the person:  ")
        time.sleep(1)
        print(phonebook[name_lookup])
    
    elif phonebook_options == "5":
        print("Good bye!")

    else: # restarts phonebook app if user inputs incorrect value
        print("Please start from the beginning and enter a valid choice.")
        time.sleep(1)
        main()

main()