# Write a script that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each word in the alphabet was used in the text. 

paragraph = input("Please write a short paragraph:  ")
words = paragraph.split() # split short paragraph by word
d = {} # define an empty dictionary


for i in set(words):
    d[i] = words.count(i) # count the number of words
print(d)