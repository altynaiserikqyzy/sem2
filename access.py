kbtu_info = {
  "name": "KBTU",
  "location": "Almaty",
  "established": 2001
}
# Accessing the value by the 'name' key
university_name = kbtu_info["name"]
print(university_name)  # Output: KBTU

university_name = kbtu_info.get("name")
print(university_name)  # Output: KBTU

keys_list = kbtu_info.keys()
print(keys_list)  # Output: dict_keys(['name', 'location', 'established'])

kbtu_info = {
  "name": "KBTU",
  "location": "Almaty",
  "established": 2001
}

keys_list = kbtu_info.keys()
print(keys_list)  # Output before change: dict_keys(['name', 'location', 'established'])

# Adding a new key-value pair
kbtu_info["rank"] = 1
print(keys_list)  # Output after change: dict_keys(['name', 'location', 'established', 'rank'])

values_list = kbtu_info.values()
print(values_list)  # Output: dict_values(['KBTU', 'Almaty', 2001])

kbtu_info = {
  "name": "KBTU",
  "location": "Almaty",
  "established": 2001
}

values_list = kbtu_info.values()
print(values_list)  # Output before change: dict_values(['KBTU', 'Almaty', 2001])

# Updating the value for 'location'
kbtu_info["location"] = "Nur-Sultan"
print(values_list)  # Output after change: dict_values(['KBTU', 'Nur-Sultan', 2001])

if "rank" in kbtu_info:
    print("Yes, 'rank' is one of the keys in the kbtu_info dictionary")