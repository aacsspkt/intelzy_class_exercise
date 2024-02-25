list = ['a', 'b', 'c', 'd']

iter = iter(list)

def lazy_returner():
    yield 'apple'
    yield 'banana'

def do_something(item):
    print(item)

# index = 0
# while index < len(list):
#     print(list[index]) 
#     index+=1

len = 10
for num in range(len):
    print("*" * (2 * num + 1 ))