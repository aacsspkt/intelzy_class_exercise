my_dict = {
    "one": 1,
    "two": 2,
    "boolean": False,
    "list": ["apple", "banana", "cherry"],
    "child": {
        "ten": 10
    },
    "name": "Aacs Spkt"
}

print("my dict:", my_dict)

# accessing values
first = my_dict["one"]
second = my_dict["two"]
print("one", first)
print("two", second)

# len of dict
dict_len = len(my_dict)
print("len", dict_len)


# add item
my_dict["three"] = 3
print("my dict:", my_dict)

# change item
my_dict["boolean"] = True
print("my dict:", my_dict)

# remove item
removed_item = my_dict.pop("three")
print("removed item:", removed_item)
print("my dict", my_dict)


# loop 
print("dict =>")
for (key, value) in my_dict.items():
    print(key, ":", value)