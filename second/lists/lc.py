fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newl=[x for x in fruits if "a" in x]
print(newl)
newl=[x for x in fruits if x != "apple"]
print(newl)
newl=[x**2 for x in range(10) if x%2==0]
print(newl)
newl=[x.upper() for x in fruits]
print(newl)
newl = [x if x != "banana" else "orange" for x in fruits]
print(newl)