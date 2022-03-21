L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate white', 17),
    ('Cakes', 19)
]

L1.sort(reverse=True)
print(L1)

print("\n***\n")

def sort_product(item):
    return item[1]
L1.sort(key=sort_product)
print(L1)

print("\n***\n")

L1.sort(key=lambda item: item[1])
print(L1)

print("\n***\n")

L1 = sorted(L1, reverse=True)
print(L1)