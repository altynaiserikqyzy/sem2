thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)
def myfunc(n):
    return abs(n-20)
wlist=[20,14,199,20,30,405,6,7,34,23]
wlist.sort(key=myfunc)
print(wlist)
wlist.reverse()
print(wlist)