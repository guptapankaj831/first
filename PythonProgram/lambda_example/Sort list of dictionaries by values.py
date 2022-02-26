# sort list of dictionaries by values

lis = [{"name": "Nandini", "age": 20}, {"name": "Manjeet", "age": 20}, {"name": "Nikhil" , "age": 19}]

print(sorted(lis, key=lambda x: x["age"]))
print(sorted(lis, key=lambda x: x["age"], reverse=True))
print(sorted(lis, key=lambda x: x["name"]))
print(sorted(lis, key=lambda x: x["name"], reverse=True))
