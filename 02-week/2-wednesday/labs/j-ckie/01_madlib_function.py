# Write a function that accepts two arguments: a name and a subject.
# The function should return a String with the name and subject interpolated in.

# For example:
# madlib("Jenn", "science") # "Jenn's favorite subject is science." madlib("Jeff", "history") # "Jeff's favorite subject is history."
# Provide default arguments in case one or both are omitted.

def madlib(name,subject):
    return f"{name}'s favorite subject is {subject}."

madlib(John,Math)
