#Simple, remove the spaces from the string, then return the resultant string.

#My solution without using methods
def no_space(x):
    new_string = ""
    for char in x:
        if char != " ":
            new_string += char
    return new_string

#Best answer:
def no_space(x):
    return x.replace(' ' ,'')
