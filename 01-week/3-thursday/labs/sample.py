# import datetime

# year_born = int(input("Enter the year you were born: "))
# now = datetime.datetime.now()
# current_year = now.year

# print("You are " + str(current_year - year_born) + " years old!")



# If over 100, say you're old
# If under 10, say you're young
# If over 100 and name is "Jackie", then say "Welcome back"
# IF anything else, say you're just in the middle somewhere

# age = int(input("What is your age?" ))
# name = input("What is your name? ")

# if age > 100 and name == "Jackie":
#     print("Welcome back")

# elif age > 100:
#     print("You're old.")

# elif age < 10:
#     print("You're young.")

# else:
#    print("You're just in the middle somewhere.")


# Loops

# bottles_of_beer = 99
# first_phrase = " bottles of beer "
# preposition = " on the wall "
# second_phrase = "Take one down, pass it around "

# while bottles_of_beer > 0:
#    print("======")
#    print(f"{bottles_of_beer} {first_phrase} {preposition}")
#    print(f"{bottles_of_beer} {first_phrase}")
#    print(f"{second_phrase}")
#    bottles_of_beer = bottles_of_beer - 1
#    print(f"{bottles_of_beer} {first_phrase} {preposition}")
#    if bottles_of_beer == 0:
#        print ("Now there's no more bottles of beer on the wall!")
#    else:
#        print(f"{bottles_of_beer} {first_phrase}")