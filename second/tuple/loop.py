first=("myname" , 12 , 12.88 , 's' , True)
#Iterate through the items and print the values:
for x in first:
    print(x)
#Print all items by referring to their index number
for i in range(len(first)):
    print(first[i])
#Print all items, using a while loop to go through all the index numbers:
i = 0 
while i < len(first):
    print(first[i])
    i+=1