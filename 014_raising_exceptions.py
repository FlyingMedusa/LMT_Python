def divide(a,b):
    '''
    input: a,b : positive int
    output : float
    '''
    if a < 0 or b < 0:
        raise ValueError
    return a/b

try:
    a = int(input('Enter a positive integer numer \'a\': ... '))
    b = int(input('Enter a positive integer numer \'b\': ... '))
    num = divide(a,b)
    print(f'The result of division {a} / {b} = {num}')
except ValueError:
    print('You didn\'t enter valid numbers!')
except ZeroDivisionError:
    print('You can\'t  divide by 0!')