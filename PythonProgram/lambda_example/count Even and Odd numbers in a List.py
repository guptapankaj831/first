# count Even and Odd numbers in a List

# Input: list1 = [2, 7, 5, 64, 14]
# Output: Even = 3, odd = 2
#
# Input: list2 = [12, 14, 95, 3]
# Output: Even = 2, odd = 2

list1 = [2, 7, 5, 64, 14]
even_list = []
odd_list = []

even = len(list(filter(lambda x: (x % 2 == 0), list1)))
odd = len(list(filter(lambda x: (x % 2 != 0), list1)))
print("Even ", even)
print("Odd ", odd)


