# Adds an element to the set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
# Removes all elements from the set
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()
# Returns a copy of the set
my_set = {1, 2, 3}
copy_set = my_set.copy()
print(copy_set)  # Output: {1, 2, 3}
# Returns the difference between two sets
set_a = {1, 2, 3}
set_b = {2, 3, 4}
result = set_a.difference(set_b)
print(result)  # Output: {1}
# Removes common elements from the original set
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_a.difference_update(set_b)
print(set_a)  # Output: {1}
# Removes the specified element; does nothing if element doesn't exist
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}
# Finds common elements between sets
set_a = {1, 2, 3}
set_b = {2, 3, 4}
result = set_a.intersection(set_b)
print(result)  # Output: {2, 3}
# Keeps only common elements in the original set
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_a.intersection_update(set_b)
print(set_a)  # Output: {2, 3}
# Checks if two sets have no common elements
set_a = {1, 2}
set_b = {3, 4}
print(set_a.isdisjoint(set_b))  # Output: True
# Checks if one set is a subset of another
set_a = {1, 2}
set_b = {1, 2, 3}
print(set_a.issubset(set_b))  # Output: True
print(set_a < set_b)  # Output: True
# Checks if one set is a superset of another
set_a = {1, 2, 3}
set_b = {1, 2}
print(set_a.issuperset(set_b))  # Output: True
print(set_a > set_b)  # Output: True
# Removes and returns an arbitrary element
my_set = {1, 2, 3}
popped_element = my_set.pop()
print(popped_element)  # Output: 1 (or any random element)
print(my_set)  # Output: Remaining elements
# Removes the specified element; raises KeyError if not found
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}
# Finds elements in either set but not both
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a.symmetric_difference(set_b)
print(result)  # Output: {1, 2, 4, 5}
# Updates a set with elements that are unique to either set
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_a.symmetric_difference_update(set_b)
print(set_a)  # Output: {1, 2, 4, 5}
# Combines all unique elements from both sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a.union(set_b)
print(result)  # Output: {1, 2, 3, 4, 5}# Adds all unique elements from another set to the original set
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_a.update(set_b)
print(set_a)  # Output: {1, 2, 3, 4, 5}