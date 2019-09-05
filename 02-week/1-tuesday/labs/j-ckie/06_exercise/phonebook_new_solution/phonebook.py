from save import *
import time

def back(phonebook): # REMEMBER THE PARANTHESES AT THE END OF .UPPER() THIS WILL BREAK WITHOUT IT
    previous = input("Would you like to return to the previous menu? Y/N  ").upper()
    if previous == "Y":
        print("Redirecting...")
        time.sleep(.5)
        main() # find out why this breaks when back function is in separate file
    else:
        print("Good bye!")
        save(phonebook)

def main():
    phonebook = init()
    
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
    menu_options = int(input("What would you like to do? Select 1 - 5  "))

    if menu_options == 1:
        name_lookup = input("Enter the name of the person:  ").upper()
        if name_lookup in phonebook:
            print("This person's number is:  ", phonebook[name_lookup])
            time.sleep(.2)
            back(phonebook)
        else:
            print("Please enter a valid name")
            time.sleep(1)
            main()
    
    elif menu_options == 2:
        print("Please fill in the information below:")
        new_name = input("Name:  ").upper()
        new_num = input("Number:  ")
        phonebook.update({new_name : new_num})
        time.sleep(.2)
        print(f"Entry stored for {new_name}")
        save(phonebook)
        back(phonebook)
    
    elif menu_options ==3:
        print("Please fill in the information below:")
        name_del = input("Enter the name of the person who's information you'd like to delete:  ").upper()
        if name_del in phonebook:
            confirm = input("You are about to delete a person's information. This action cannot be undone. Are you sure? (Y/N)  ").upper()
            if confirm == "Y":
                print("Now deleting...")
                time.sleep(1)
                del phonebook[name_del]
                save(phonebook) # call save function to save dictionary changes
                back(phonebook)
            else:
                print("Now redirecting to main menu...")
                time.sleep(1)
                main() # call main function to restart from beginning
        else:
            print("Please enter a valid person.")
            time.sleep(1)
            main()

    elif menu_options == 4:
        for key,val in phonebook.items():
            print("Found entry for " + key + ": " + val)
        time.sleep(.5)
        main()

    elif menu_options == 5:
        print("Good bye!")
        save(phonebook)

    else:
        print("Please choose a valid option")
        main()
        
main()

