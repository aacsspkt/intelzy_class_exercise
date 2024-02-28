file = open("hello.txt", "r")

# data = file.read()

# print(data)

# print("closed", file.closed)

# print("closed", file.closed)

# data = file.readlines()

# for line in data:
#     print(line, end="")

# data = file.readline()
# print("data:", data)

# data = file.readline()
# print("data:", data, end="")

for line in file:
    print(line)

file.close()