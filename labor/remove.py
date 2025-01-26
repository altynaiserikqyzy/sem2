thisset = {"apple", "banana", "cherry", True, 1, 2}
#To remove an item in a set, use the remove(), or the discard() method
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)
thisset.add("banana")
x = thisset.pop()
print(x)
print(thisset)
#The clear() method empties the set:
thisset.clear()
print(thisset)
#The del keyword will delete the set completely
del thisset

print(thisset)