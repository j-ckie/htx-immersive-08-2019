import pickle
import init
import save

def back_to_main_menu(phonebook):
    menu_restart = "Would you like to go to the previous menu? (Y / N)  "

    app_restart = input(menu_restart).upper()
    if app_restart == "Y":
        print("Redirecting...")
        time.sleep(1)
        main()
    else:
        print("Good bye!")
        save(phonebook)
        