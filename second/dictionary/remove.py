student_info = {
  "name": "John",
  "age": 18,
  "city": "New York"
}

# Remove 'age' using pop()
student_info.pop("age")
print(student_info)

book_info = {
  "title": "1984",
  "author": "George Orwell",
  "year": 1949
}

# Remove the last inserted item using popitem()
book_info.popitem()
print(book_info)

country_info = {
  "name": "Japan",
  "capital": "Tokyo",
  "population": 126.8
}

# Remove 'capital' using del
del country_info["capital"]
print(country_info)

fruit_info = {
  "name": "Apple",
  "color": "Red",
  "taste": "Sweet"
}

# Delete the entire dictionary using del
del fruit_info
# Trying to print fruit_info now will cause an error because the dictionary no longer exists
# print(fruit_info)  # This will cause an error

person_info = {
  "name": "Alice",
  "age": 30,
  "occupation": "Engineer"
}

# Clear all items from the dictionary using clear()
person_info.clear()
print(person_info)

