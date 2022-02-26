# Convert List of Dictionaries to List of Lists

# Input : test_list = [{‘Gfg’: 123, ‘best’: 10}, {‘Gfg’: 51, ‘best’: 7}]
# Output : [[‘Gfg’, ‘best’], [123, 10], [51, 7]]

test_list = [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}]

# Method #1 : Using loop + enumerate()
final_list = []
for ind, val in enumerate(test_list):
    if ind == 0:
        final_list.append(list(val.keys()))

    final_list.append(list(val.values()))

print(final_list)

# Method #2 : Using list comprehension

final_list = [[i for i in test_list[0].keys()], *[list(j.values()) for j in test_list]]
print(final_list)


