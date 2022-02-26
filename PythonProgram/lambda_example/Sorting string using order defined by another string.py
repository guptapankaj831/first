# Sorting string using order defined by another string
# Input : pat = "asbcklfdmegnot", str = "eksge"
# Output : str = "geeks"
# (after sorting, str becomes "skeeg" and return its reverse)
#
# Input : pat = "mgewqnasibkldjxruohypzcftv", str = "niocgd"
# Output : str = "coding"

pat = "mgewqnasibkldjxruohypzcftv"
st = "niocgd"

pat_list = list(pat)
st_list = list(st)

pat_dict = {pat_list[i]: i for i in range(len(pat_list))}

st_list.sort(key=lambda x: pat_dict[x])
st_list.reverse()
print(''.join(st_list))


