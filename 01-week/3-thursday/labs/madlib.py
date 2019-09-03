import time

#Madlibs
print("Let's play a Madlib!")
time.sleep(2)
print("Please fill in the blanks below:")
print("__[NAME]__'s favorite subject in school is __[SUBJECT]__.")
madlib_name = input("What is the person's name?  ")
madlib_subject = input("What is the school subject?  ")
print(madlib_name + "'s favorite subject in school is " + madlib_subject + ".")