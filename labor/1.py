#1
print(90 > 9)
print(90 == 9)
print(90 < 9)
#2
a = 78
b = 98

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#3
print(bool("KBTU"))
print(bool(0))
#4
x = "KBTU"
y = 10000

print(bool(x))
print(bool(y))
#5
#1 they will return true because there are some values ​​there and they are not empty
bool("abc")
bool(102030405060760)
bool(["uni", "pp", "lab"])
#2and these will return false since the print arguments here are empty lists and logical false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#6
class MyContainer():#my object , new class
    def __len__(self):
        return 0

container = MyContainer()
print(bool(container))  # False
 
#7
def TrueorFalse():
   return True
print(TrueorFalse())
#8 
if(TrueorFalse):
   print("YES")
else:
   print("Oh no , fake :( ")
#9
x = "rg"
print(isinstance(x, str))
#10