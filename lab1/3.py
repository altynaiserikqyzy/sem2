thislist = [ "int" , "str" , "float" , "items"]
print(thislist)
print(thislist[0])
thislist = thislist.sort()
print(thislist)
thislist[1]=thislist[-1]
print(len(thislist))
#2
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))
list2=list("apple" , "bnn" , "orange")
print(list2)
my_tuple = (1, 2, 3, 4, 5, 3)
print("Tuple:", my_tuple)
my_set = {1, 2, 3, 4, 5, 3}  # Дубликат 3 
print("Set:", my_set)
my_dict = {"name": "Altynai", "age": 20, "city": "Semey"}
print("Dictionary:", my_dict)
my_dict["age"] = 21  
print("Updated Dictionary:", my_dict)