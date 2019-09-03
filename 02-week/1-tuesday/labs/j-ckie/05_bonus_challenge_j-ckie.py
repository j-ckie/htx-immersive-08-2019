# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters

word = input("Input a word:  ")

dictionary = {}

for i in set(word): # for characters in inputted word
    dictionary[i] = word.count(i) # use .count to tally number of individual characters

print(f"The word {word} is broken down like this: ")
print(dictionary)