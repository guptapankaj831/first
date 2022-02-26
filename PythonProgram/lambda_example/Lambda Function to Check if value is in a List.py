# Lambda Function to Check if value is in a List

# Input  :  L = [1, 2, 3, 4, 5]
#           element = 4
# Output :  Element is Present in the list

# Input  :  L = [1, 2, 3, 4, 5]
#           element = 8
# Output :  Element is NOT Present in the list

L = [1, 2, 3, 4, 5]
element = 5
check = lambda arr, x: "Yes" if x in arr else "No"
print(check(L, element))



