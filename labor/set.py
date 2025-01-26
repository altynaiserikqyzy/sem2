#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#Get the number of items in a set:
print(len(thisset))
#A set can contain different data types
set1 = {"abc", 34, True, 40, "male"}
#data type of a set
print(type(set1))
#
fruits = set(("apple", "banana", "cherry")) # note the double round-brackets
print(fruits)