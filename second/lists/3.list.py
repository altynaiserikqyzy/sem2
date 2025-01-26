list1 = ["abc", 34, True, 40, "female"]
#1 access list items
print(type(list1))
print(list1[1])
print(list1[-1])
print(list1[1:4])
print(list1[2:])
print(list1[:4])
if "abc" in list1:
  print("Yes, 'abc' is in the list")
#2 change list items , add
list1[1]="right"
list1[2:4] = [False, "watermelon"]
list1.insert(2,"male")
list1.append(200)
#3 extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#remove pop list
thislist.remove("papaya")
thislist.pop(1)
#4 
for x in thislist:
  print(x)
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

