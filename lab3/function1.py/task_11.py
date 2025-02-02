def palimdrom(a):
    text = ''.join(char.lower() for char in a if char.isalnum())
    return text == text[::-1]

