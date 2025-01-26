thisset = {"apple", "banana", "cherry", True, 1, 2}
#Add an item to a set, using the add() method:
thisset.add("open")
print(thisset)
#To add items from another set into the current set, use the update() method.
set1 = {1, 2, 3, "apple", "banana"}
set2 = {"banana", 4, 5, 6, True}
set1.update(set2)
print(set1)