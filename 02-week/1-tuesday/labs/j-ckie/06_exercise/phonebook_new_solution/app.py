# $ python phonebook.py 
# Electronic Phone Book 
# ===================== 
# 1. Look up an entry 
# 2. Set an entry 
# 3. Delete an entry 
# 4. List all entries 
# 5. Quit

import time
import os.path
import pickle
import init
import menu
import save


phonebook = init.init() # run init function to check if data file is created, if not, create data file

choice = menu.selection()

# while choice != 5:
if choice == 1:
    # 1. Look up an entry
    print("Test")
    time.sleep(3)
    menu.menu()
    

# else:
#     print("Please select a valid option")
#     menu.selection()

    # 5. Quit
print("Good bye!")
    
