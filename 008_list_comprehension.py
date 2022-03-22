even_list = [ i for i in range(10) if i % 2 == 0]
print(even_list)

filtered_list = [ x for x in range(50) if x % 2 == 0 if x % 5 == 0]
print(filtered_list)

list = ["even" if y%2==0 else "odd" for y in range(5)]
print(list)

#Finding Transpose of a Matrix
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose_matrix = [[row[i] for row in matrix] for i in range(2)]
print (transpose_matrix)

names = ['Ch','Dh','Ehg','cb','Tb','Td','Chb','Tdb']
final_names = [name for name in names if name.lower().endswith('b') and len(name) > 2]
print(final_names)

# Reverse each elements in a specified tuple
List = [string[::-1] for string in ('Hello', 'Analytics', 'Vidhya')]
print(List)