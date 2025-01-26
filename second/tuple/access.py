tuple1=("apple" , 12 , 'n' , 12.98 , "string" , "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple1[1])
#Negative Indexing
print(tuple1[-1])
#Range of Indexes
print(tuple1[2:5])
print(tuple1[:4])
print(tuple1[2:])
#Range of Negative Indexes
print(tuple1[-4:-1])
if 12.98 in tuple1:
    print("YES , 12.98 in tuple1")
else:
    print("no , 12.98 is not in tuple1")