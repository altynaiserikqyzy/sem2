import time
import math
num = int(input('enter the number: '))
delay = int(input("enter the delay : "))
time.sleep(delay/1000)
res = math.sqrt(num)
print(f"Квадратный корень {num} после {delay} миллисекунд: {res}")