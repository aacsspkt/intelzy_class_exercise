spr = ["scissor", "paper", "rock", "scissor"]

print("spr:", spr)

# spr.append("mud")
# print("spr:", spr)

# item = spr.pop()
# print("popped item:", item)
# print("spr:", spr)

# print("scissor count:", spr.count("paper"))

# fruits = ["apple", "banana", "orange"]
# spr.extend(fruits)
# # new = spr + fruits
# print("spr", spr)

# spr.remove("apple")
# print("spr", spr)

# another_spr = spr.copy()
# print("another spr:", another_spr)

# i = spr.index("paper")
# print("paper is at index:", i)

# spr.reverse()
# print("spr", spr)

# sort ascending
spr.sort() 
print("spr sorted", spr)

num_list = [10, 9, 6, 20, 7]
num_list.sort()
print("num sorted", num_list)

# sort descending
spr.sort(reverse=True)
print("spr sorted", spr)

spr.clear()
print("spr", spr)

second = spr[1]
print()