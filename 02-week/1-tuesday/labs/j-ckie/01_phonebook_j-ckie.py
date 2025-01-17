# Given the following dictionary, representing a mapping from names to phone numbers:

# phonebook_dict = { 
#   'Alice': '703-493-1834', 
#   'Bob': '857-384-1234', 
#   'Elizabeth': '484-584-2923'
# }
# Write code to do the following:

# Print Elizabeth's phone number.
# Add a entry to the dictionary: Kareem's number is 938-489-1234.
# Delete Alice's phone entry.
# Change Bob's phone number to '968-345-2345'.
# Print all the phone entries.

phonebook_dict = { 
    "Alice": "703-493-1834", 
    "Bob": "857-384-1234", 
    "Elizabeth": "484-584-2923"
 }

for key,val in phonebook_dict.items():
    print("Found original entries for " + key + ": " + val)

print(phonebook_dict["Elizabeth"]) # print Elizabeth's number

phonebook_dict.update( {"Kareem" : "938-489-1234"} ) # add Kareem's info to the dictionary

del phonebook_dict["Alice"] # remove Alice's info

phonebook_dict["Bob"] = "968-345-2345" # change Bob's phone number

for key,val in phonebook_dict.items():
    print("Found entry for " + key + ": " + val)