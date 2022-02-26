# Convert Key-Value list Dictionary to Lists of List

# Input ->  {'gfg' : [1, 3, 4], 'is' : [7, 6], 'best' : [4, 5]}
# Output -> [[‘gfg’, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]

# Method #1 : Using loop + items()
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

final_dict = []

for key, val in test_dict.items():
    final_dict.append([key] + val)

print(final_dict)

# Method #2 : Using list comprehension
final_dict = [[key] + val for key, val in test_dict.items()]
print(final_dict)
