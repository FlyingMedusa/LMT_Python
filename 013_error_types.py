'''
Basics: 
• NameError: local or global name not found,
• TypeError: operand does not have correct type,
  e.g., list -> int / "a"/4
• ValueError: value is illegal,
• IndexError: if index out of range,
• IOError: IO system error, e.g., file not found
• ZeroDivisionError: if you try to divide a numer by zero
https://docs.python.org/3/library/exceptions.html
'''

#value error
# num = int('a')
# print(f'Our number is {num}')

#type error
# num = int([1, 3, 6])
# print(f'Our number is {num}')

# IOError-> FileNotFoundError
# file = open('ztest.py')
# print('File is opened')
# file.close()

# handling ValueError and ZeroDivisionError
try:
    a = int(input('Enter the integer numer \'a\': ... '))
    b = int(input('Enter the integer numer \'b\': ... '))
    num = a / b
    print(f'The result of division {a} / {b} = {num}')
except ValueError:
    print('You didn\'t enter a valid number!')
except ZeroDivisionError:
    print('You can\'t  divide by 0!')

# working with resources
try:
    file = open('test.py')
    a = int(input('Enter the integer numer \'a\': ... '))
    b = int(input('Enter the integer numer \'b\': ... '))
    num = a / b
    print(f'The result of division {a} / {b} = {num}')
    print('Writting the result to the file .... ')
except ValueError:
    print('You didn\'t enter the valid number!')
except ZeroDivisionError:
    print('You can\'t  divide by 0!')
except:
    print('Something went very wrong!') 
finally:
    file.close()
    print('File is closed!')