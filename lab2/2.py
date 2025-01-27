x = 100
y = 2
print(x+y)
print(x/y)
print(x//y)
print(x%y)
print(x*y)
print(x**y)
#2
x = 1000000
x += 3
x -= 3
x *= 2
x /= 2
x %= 3
x *= 2000000
x //= 2
x = int(x)
x &= 3
x |= 3
x ^= 3
x >>= 3
print(x)
#3
a = 5  # 0101 в двоичной системе
b = 3  # 0011 в двоичной системе
print(f"a & b = {a & b}")  # 0001 → 1
print(f"a | b = {a | b}")  # 0111 → 7
print(f"a ^ b = {a ^ b}")  # 0110 → 6
print(f"~a = {~a}")  # Инвертируем биты: -6
print(f"a << 2 = {a << 2}")  # Сдвиг на 2 позиции влево: 0101 -> 010100 → 20
# Сдвиг вправо
print(f"a >> 2 = {a >> 2}")  # Сдвиг на 2 позиции вправо: 0101 -> 0001 → 1
#4 EXERCISES
#1
print(10 * 5)

#2
print(10 /2)

#3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")
  
#4
if 5 != 10:
    print("5 and 10 is not equal")
    
#5
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")