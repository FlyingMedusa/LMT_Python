def filter_list(filter_criteria, items):
    price_filtered = []
    for item in items:
        if item[1] > filter_criteria:
            price_filtered.append(item)
    return price_filtered


L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate white', 17),
    ('Cakes', 19)
]

print(filter_list(15, L1))