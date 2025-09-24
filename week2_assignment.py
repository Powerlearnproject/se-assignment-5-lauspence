my_list = []
elements = [10, 20, 30, 40]

# Step 1: Extend the list with initial elements
my_list.extend(elements)

# Step 2: Insert 15 at the second position (index 2)
my_list.insert(2, 15)

# Step 3: Extend with [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 4: Remove the last element
my_list.pop()

# Step 5: Sort the list
my_list.sort()

# Step 6: Find and print index of 30
if 30 in my_list:
    print("Index of 30:", my_list.index(30))
else:
    print("30 is not in the list.")

# Final output
print("Final list:", my_list)
