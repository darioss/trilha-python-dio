list = [1, "Python", [40, 30, 20]]

list2 = list.copy()

print(f"Original List: {id(list)} - {list}")  # [1, "Python", [40, 30, 20]]
print(f"Copy: {id(list2)} - {list2}")

list[0] = 2
print(list)
print(list2)