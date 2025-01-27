a = 33
b = 200
if b > a:
    print("b is greater than a")  # If b is greater than a, print this

a = 33
b = 200
if b > a:
    print("b is greater than a")  

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")  # If a equals b, print this

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")  # If neither condition is true, print this

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")  # If b is not greater than a, print this

if a > b: print("a is greater than b")  # One-line if statement

a = 2
b = 330
print("A") if a > b else print("B")  # Ternary operator: if a > b print "A", else print "B"

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")  # Multiple conditions in one line

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")  # Both conditions must be true

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")  # At least one condition must be true

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")  # If a is NOT greater than b, print this

x = 41

if x > 10:
    print("Above ten,")  # If x is greater than 10, print this
    if x > 20:
        print("and also above 20!")  # If x is also greater than 20, print this
    else:
        print("but not above 20.")  # Otherwise, print this

a = 33
b = 200

if b > a:
    pass  # Do nothing if b is greater than a
