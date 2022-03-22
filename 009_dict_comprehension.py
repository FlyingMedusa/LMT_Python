words = ['data', 'science', 'machine', 'learning']
words_len = {i:len(i) for i in words}
print(words_len)

words_len = {i:len(i) for i in words if len(i) > 5}
print(words_len)

words_dict = {i:len(i) if len(i) > 5 else 'short' for i in words}
print(words_dict)

words = ['data', 'science', 'machine', 'learning']
values = [5, 3, 1, 8]
dict_a = {i:j for i, j in zip(words, values)}
print(dict_a)

dict_a = {i:j for i, j in zip(words, values) if j > 4}
print(dict_a)

dict_b = {i.upper():j**2 for i, j in zip(words, values)}
print(dict_b)
print(dict_b.items())

dict_c = {i.lower():j%2 for i, j in dict_b.items()}
print(dict_c)

names = ['John', 'Jane', 'Adam', 'Eva', 'Ashley']
print(list(enumerate(names)))
print(dict(enumerate(names)))
dict_names = {i:len(j) for i, j in enumerate(names)}
print(dict_names)

lst = ['data','science','artificial', 'intelligence']
dct = {'data': 5, 'science': 3, 'machine': 1, 'learning': 8}
print({i:dct[i] if i in dct else len(i) for i in lst})

a = [1,2,3,4]
b = [5,6,7]
dct = {(i,j):i*j for i in a for j in b}
print(dct)