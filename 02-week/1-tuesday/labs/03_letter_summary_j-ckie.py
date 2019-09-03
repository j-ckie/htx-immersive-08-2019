# Write a script that takes a word as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the word.

word = input("Input a word:  ")

dictionary = {}

for i in set(word): # for characters in inputted word
    dictionary[i] = word.count(i) # use .count to tally number of individual characters
print(dictionary)