def letters(string):
    upper = 0 
    lower = 0
    for i in string:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
    return upper , lower
a = "HEllO WoRLd"
print(letters(a))
