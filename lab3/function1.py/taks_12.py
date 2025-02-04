def histogram(LISTS):
    for i in LISTS:
        print('*'*i)
b=[3,4,5]
histogram(b)
def histogram(numbers):
    result = []  # Initialize an empty list to store histogram strings
    for num in numbers:
        result.append('*' * num)  # Add each line of asterisks to the list
    return result  # Return the list of histogram strings

