# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters
from collections import OrderedDict

word = input("Input a word:  ")

dictionary = {}

for i in set(word): # for characters in inputted word
    dictionary[i] = word.count(i) # use .count to tally number of individual characters

print(f"The word {word} is broken down like this: ")

top_three_letters = OrderedDict() # create an ordered dictionary -> VERY IMPORTANT

for key, value in sorted(dictionary.items(), key=lambda item : item[1]): # sort letters from smallest to biggest
    print("%s: %s" % (key, value))
    top_three_letters.update({key : value})

letters = list(top_three_letters.items()) # spit out ordered list

print(f"The top three letters in {word} are:  ")
print(letters[-1])
print(letters[-2])
print(letters[-3])


