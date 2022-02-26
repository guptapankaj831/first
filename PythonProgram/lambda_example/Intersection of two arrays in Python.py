# Intersection of two arrays in Python ( Lambda expression and filter function )

# Input:  arr1[] = [1, 3, 4, 5, 7]
#         arr2[] = [2, 3, 5, 6]
# Output: Intersection : [3, 5]

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]

print(list(filter(lambda x: x in arr1, arr2)))
