#week 1
# Create a list
my_list = [10, 20, 30, 40, 50]

# Manipulate (add, remove, change)
my_list.append(60)
my_list.remove(30)
my_list[1] = 25

# Slicing
print("Full List:", my_list)
print("Slice [1:4]:", my_list[1:4])

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Add elements from list2 to list1
list1.extend(list2)
print("Combined List:", list1)

# Create matrix
matrix = [list1, list2]
print("Matrix:", matrix)

# Create a tuple
tup1 = (10, 20, 30, 40, 50)

# Slicing (manipulation not allowed)
print("Original Tuple:", tup1)
print("Slice [1:4]:", tup1[1:4])

# Combine two tuples
tup2 = (60, 70)
combined = tup1 + tup2
print("Combined Tuple:", combined)

# Create tuple matrix
matrix_tup = (tup1, tup2)
print("Tuple Matrix:", matrix_tup)

# Create and manipulate dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Add and modify
my_dict['d'] = 4
my_dict['b'] = 20
del my_dict['c']

print("Updated Dictionary:", my_dict)

# Merge two dictionaries
dict2 = {'e': 5, 'f': 6}
my_dict.update(dict2)
print("Merged Dictionary:", my_dict)

# Create matrix-like structure with dictionary
matrix_dict = {'row1': [1, 2], 'row2': [3, 4]}
print("Dictionary Matrix:", matrix_dict)

