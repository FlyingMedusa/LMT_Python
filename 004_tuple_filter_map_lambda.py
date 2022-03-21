some_list = [1,2,3,4]
print(list(map(lambda number: number**3, some_list)))

print("\n***\n")

L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate white', 17),
    ('Cakes', 19)
]

L2 = list(map(lambda item: item[1], L1))
print(L2)

L3 = list(map(lambda item: (item[0], item[1]*1.2), L1))
print(L3)

L4 = list(filter(lambda item: item[1] > 15, L1))
print(L4)