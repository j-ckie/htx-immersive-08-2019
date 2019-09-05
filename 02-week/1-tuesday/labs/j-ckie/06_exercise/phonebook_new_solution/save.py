# save changes to file

import pickle
import os.path

def init():
    # check if file exists
    if os.path.exists("data.pickle"):
        with open("data.pickle", "rb") as handle:
            phonebook = pickle.load(handle)
    
    else:
        # create pickle file if it does not exist
        phonebook = { 
            "ALICE": "703-493-1834", 
            "BOB": "857-384-1234", 
            "ELIZABETH": "484-584-2923",
            "JARED" : "555-987-2350",
            "ANGELA" : "555-872-9410",
            "MELISSA" : "555-554-5523"
        }
        # saves file
        with open("data.pickle", "wb") as handle: # store data to external file
            pickle.dump(phonebook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return phonebook

def save(phonebook):
    with open("data.pickle", "wb") as handle: # store data to external file -> "wb" means "write" "binary"
        pickle.dump(phonebook, handle, protocol=pickle.HIGHEST_PROTOCOL)