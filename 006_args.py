def summarize(*numbers):
    sum=0
    for n in numbers:
        sum += n
        return sum


print(f'the sum of the numbers is {summarize(1,2,3,4,5)}')
print("\n***\n")

numbers = [1,2,5,7,9,9,9,9,9,9]
first_num, second_num, *others = numbers
print(first_num)
print(others)
print("\n***\n")

numbers = [1,2,5,7,9,9,9,9,9,9,100]
first_num, *others, last_num = numbers
print(others)
print(last_num)