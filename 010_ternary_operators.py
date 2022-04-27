# var_1 = stat_if_true if condition else statement_if_false 
temperature, c_time = 100, 5
egg = 'boiled_egg' if temperature == 100 and c_time == 5 else 'raw_egg'
print(egg)

# Nested ternary operator
a, b = 10, 20
print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")

# with print
a, b = 5, 7
print(a,"is greater") if (a>b) else print(b,"is Greater")