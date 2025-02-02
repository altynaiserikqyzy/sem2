def reversed(string):
    words=string.split()
    words.reverse()
    return ' '.join(words)
a=str(input())
print(reversed(a))