# save changes to file

import pickle

def save():
    with open("data.pickle", "wb") as handle: # store data to external file -> "wb" means "write" "binary"
        pickle.dump(phonebook, handle, protocol=pickle.HIGHEST_PROTOCOL)