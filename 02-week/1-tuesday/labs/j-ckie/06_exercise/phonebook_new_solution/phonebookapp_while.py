from mainmenu import *
from picklefunk import *
import time
import os

phonebook = init()

menu_options = 2

while menu_options != "5":
    menu_options = menu()
    
    if menu_options == "1":
        name_lookup = input("Enter the name of the person:  ").upper()
        if name_lookup in phonebook:
            print("This person's number is:  ", phonebook[name_lookup])
            time.sleep(.2)
            if back(phonebook):
                continue
        else:
            print("Please select a valid person.")
            time.sleep(1.3)
            os.system('clear||cls')
            continue

    elif menu_options == "2":
        print("Please fill in the information below:")
        new_name = input("Name:  ").upper()
        new_num = input("Number:  ")
        phonebook.update({new_name : new_num})
        time.sleep(.2)
        print(f"Entry stored for {new_name}")
        save(phonebook)
        if back(phonebook):
            continue

    elif menu_options == "3":
        print("Please fill in the information below:")
        name_del = input("Enter the name of the person who's information you'd like to delete:  ").upper()
        if name_del in phonebook:
            confirm = input("You are about to delete this person's information. This action cannot be undone. Are you sure? (Y/N)  ").upper()
            if confirm == "Y":
                print("Now deleting...")
                time.sleep(1)
                del phonebook[name_del]
                save(phonebook) # call save function to save dictionary changes
                if back(phonebook):
                    continue
            else:
                print("Now redirecting to main menu...")
                time.sleep(1)
                os.system('clear||cls')
                continue 
        else:
            print("Please enter a valid person.")
            time.sleep(1.3)
            os.system('clear||cls')
            continue

    elif menu_options == "4":
        for key,val in phonebook.items():
            print("Found entry for " + key + ": " + val)
        time.sleep(.5)
        if back(phonebook):
            continue
        #     break
    elif menu_options == "5":
        print("Good bye!")
        save(phonebook)
        time.sleep(1)
        os.system('clear||cls')
        quit()
    else:
        print("Please choose a valid option.")
        time.sleep(1.3)
        os.system('clear||cls')
        continue


