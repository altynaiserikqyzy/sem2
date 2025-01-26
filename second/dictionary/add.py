car_info = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Adding a new item 'color'
car_info["color"] = "red"
print(car_info)

car_info = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Using update() to add the 'color' item
car_info.update({"color": "red"})
print(car_info)