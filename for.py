fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)  # Prints each fruit in the list

for x in "banana":
    print(x)  # Prints each character in the string

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)  # Print the fruit
    if x == "banana":
        break  # Stop the loop when x is "banana"

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break  # Exit before printing "banana"
    print(x)  # Print the fruit

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue  # Skip printing "banana"
    print(x)  # Print the fruit, skipping "banana"

for x in range(6):
    print(x)  # Prints numbers from 0 to 5
for x in range(2, 6):
    print(x)  # Prints numbers from 2 to 5 (not including 6)
for x in range(2, 30, 3):
    print(x)  # Prints numbers starting from 2 and incrementing by 3

for x in range(6):
    print(x)  # Print each number
else:
    print("Finally finished!")  # Runs after the loop completes
for x in range(6):
    if x == 3:
        break  # Stops the loop when x is 3
    print(x)  # Prints numbers from 0 to 2
else:
    print("Finally finished!")  # This will NOT run because of break

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)  # Prints each adjective for each fruit

for x in [0, 1, 2]:
    pass  # This loop does nothing, but avoids an error