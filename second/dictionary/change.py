agatha_christie = {
  "title": "Murder on the Orient Express",
  "author": "Agatha Christie",
  "year": 1934
}

# Change the year
agatha_christie["year"] = 2022
print(agatha_christie)  # Output: {'title': 'Murder on the Orient Express', 'author': 'Agatha Christie', 'year': 2022}

agatha_christie = {
  "title": "Murder on the Orient Express",
  "author": "Agatha Christie",
  "year": 1934
}

# Use update() to change the title and author
agatha_christie.update({"title": "The ABC Murders", "author": "Anonymous"})
print(agatha_christie)  # Output: {'title': 'The ABC Murders', 'author': 'Anonymous', 'year': 1934}