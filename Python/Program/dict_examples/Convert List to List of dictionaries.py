# Convert List to List of dictionaries

# Input  : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]

test_list = ['Gfg', 3, 'is', 8]
key_list = ['name', 'id']

# Method #1 : Using loop + dictionary comprehension
final_list = []
for i in range(0, len(test_list), 2):
    final_list.append({key_list[0]: test_list[i], key_list[1]: test_list[i+1]})

print(final_list)

# Method #2 : Using dictionary comprehension + list comprehension
final_list = [{key_list[0]: test_list[i], key_list[1]: test_list[i+1]} for i in range(0, len(test_list), 2)]
print(final_list)
