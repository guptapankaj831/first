# rearrange positive and negative numbers

# Input :  arr[] = [12, 11, -13, -5, 6, -7, 5, -3, -6]
# Output : arr[] = [-13, -5, -7, -3, -6, 12, 11, 6, 5]

arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]

print([x for x in arr if x < 0] + [x for x in arr if x > 0])
