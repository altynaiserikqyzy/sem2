def threes(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i]==3 and numbers[i+1]==3:
            return True
    return False
a=[]
for i in range(10):
    s = int(input())
    a.append(s)
result=threes(a)
print(result)