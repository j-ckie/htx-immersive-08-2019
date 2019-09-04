import pickle
import os.path

def init():
# check if file exists
    if os.path.exists("data.pickle"):
        with open("data.pickle", "rb") as handle:
            phonebook = pickle.load(handle)
    
    else:
        # phonebook initialization if pickle file does not exist
        phonebook = { 
            "Alice": "703-493-1834", 
            "Bob": "857-384-1234", 
            "Elizabeth": "484-584-2923",
            "Jared" : "555-987-2350",
            "Angela" : "555-872-9410",
            "Melissa" : "555-554-5523"
        }
        # saves file
        with open("data.pickle", "wb") as handle: # store data to external file
            pickle.dump(phonebook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return phonebook