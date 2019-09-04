import pickle
import init

#save file
def save(phonebook):
        with open("phonebook_app.pickle", "wb") as handle: # store data to external file -> "wb" means "write" "binary"
            pickle.dump(phonebook, handle, protocol=pickle.HIGHEST_PROTOCOL)