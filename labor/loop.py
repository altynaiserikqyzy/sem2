thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
for x in thislist:
    print(x)
thislist.pop()
for i in range(len(thislist)):
    print(thislist[i])
i = 0
while i < len(thislist):
    print(thislist[i])
    i+=1
[print(x) for x in thislist]