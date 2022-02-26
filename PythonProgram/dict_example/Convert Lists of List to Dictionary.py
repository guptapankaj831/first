# Convert Lists of List to Dictionary
# Input  -> test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# Output -> {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}

test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

# Method #1 : Using loop
final_dict = {}

for i in test_list:
    final_dict[tuple(i[:2])] = tuple(i[2:])
print(final_dict)


# Method #2 : Using dictionary comprehension
final_dict = {tuple(i[:2]): tuple(i[2:]) for i in test_list}
print(final_dict)
