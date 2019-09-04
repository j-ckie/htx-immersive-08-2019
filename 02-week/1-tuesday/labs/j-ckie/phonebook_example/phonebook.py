from data import entries
import menu

selection = menu.menu_selection()

while selection != 5:
    # Do code
    if selection == 1:
       # 1. Look up entry
       lookup_by_name(
           input("What name do you want to look up?  ").capitalize
       )
       
       pass
    elif selection == 2:
        # 2. Set an entry
        pass
    elif selection == 3:
        # 3. Delete all entries
        pass
    elif selection == 4:
        # 4. List all entries
        pass
    elif selection == 5:
        # 5. Quit
        break
    else:
        print("Please try again")
        selection.menu.menu_selection()
        
    selection.menu.menu_selection()

print("Good bye!")