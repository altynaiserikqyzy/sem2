tuple1=(11 , 12 , 13 , 14 , 15)
print(tuple1)
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1))
thistuple=(tuple(("apple" , "banana" , "strawberry")))
print(thistuple)
y = ("st",)
thistuple+=y
print(thistuple)
y=list(thistuple)
y.remove("banana")
thistuple=tuple(y)
print(thistuple)