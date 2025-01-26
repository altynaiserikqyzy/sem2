mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict.clear()
print(mydict)  # Output: {}

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
copied_dict = mydict.copy()
print(copied_dict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

keys = ("name", "age", "city")
value = "Unknown"
mydict = dict.fromkeys(keys, value)
print(mydict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
value = mydict.get("model")
print(value)  # Output: Mustang

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
items = mydict.items()
print(items)  # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
keys = mydict.keys()
print(keys)  # Output: dict_keys(['brand', 'model', 'year'])

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
removed_value = mydict.pop("model")
print(removed_value)  # Output: Mustang
print(mydict)  # Output: {'brand': 'Ford', 'year': 1964}

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
last_item = mydict.popitem()
print(last_item)  # Output: ('year', 1964)
print(mydict)  # Output: {'brand': 'Ford', 'model': 'Mustang'}

mydict = {"brand": "Ford", "model": "Mustang"}
value = mydict.setdefault("year", 1964)
print(value)  # Output: 1964
print(mydict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

mydict = {"brand": "Ford", "model": "Mustang"}
mydict.update({"year": 1964, "color": "red"})
print(mydict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
values = mydict.values()
print(values)  # Output: dict_values(['Ford', 'Mustang', 1964])