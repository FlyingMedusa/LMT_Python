L1 = [
    {'Name': 'Bread', 'Price': 10},
    {'Name': 'Butter', 'Price': 20},
    {'Name': 'Chocolate dark', 'Price': 15},
    {'Name': 'Chocolate white', 'Price': 17},
    {'Name': 'Cakes', 'Price': 19},
]

filtered_list = list(filter(lambda item: item['Price'] > 15, L1))
print(filtered_list)

L2 = list(map(lambda item: item['Price'], L1))
print(L2)

L3 = list(map(lambda item: (item['Name'], item['Price']*1.2), L1))
print(L3)