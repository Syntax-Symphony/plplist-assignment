# Step 1: Create an empty list
my_list = []
print( my_list)

# Step 2: Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print( my_list)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print( my_list)

# Step 4: Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])
print( my_list)

# Step 5: Remove the last element
my_list.pop()
print( my_list)

# Step 6: Sort the list in ascending order
my_list.sort()
print( my_list)

# Step 7: Find and print the index of 30
index_of_30 = my_list.index(30)
print( index_of_30)
