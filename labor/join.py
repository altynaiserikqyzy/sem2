# union() example
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Combine all unique elements from both sets into a new set
result = set_a.union(set_b)
print(result)  # {1, 2, 3, 4, 5}

# update() example
set_c = {6, 7, 8}
set_a.update(set_c)  # Adds all unique elements of set_c to set_a
print(set_a)  # {1, 2, 3, 6, 7, 8}

# intersection() example
set_x = {10, 20, 30}
set_y = {20, 30, 40}

# Find the common elements between two sets
result = set_x.intersection(set_y)
print(result)  #  {20, 30}

# difference() example
set_p = {5, 10, 15, 20}
set_q = {15, 20, 25, 30}

# Find elements that are in set_p but not in set_q
result = set_p.difference(set_q)
print(result)  # Output: {5, 10}

# symmetric_difference() example
set_m = {1, 2, 3, 4}
set_n = {3, 4, 5, 6}

# Find elements that are in either set, but not in both
result = set_m.symmetric_difference(set_n)
print(result)  # Output: {1, 2, 5, 6}