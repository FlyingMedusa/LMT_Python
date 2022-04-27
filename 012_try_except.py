def factorial(n):
    '''
    input : an int 
    output : factorial of the int (if the input is a negative integer, the function will raise an exception)
    '''
    if n < 0:
        raise ValueError
    n_factorial = 1
    for i in range(1,n+1):
        n_factorial *= i
    return n_factorial


try:
    number = int(input('Enter a positive integer number: ...'))
    print(f'{number}! = {factorial(number)}')
except ValueError:
    print('Enter a POSITIVE INTEGER!')
    print(f'{number}! => ERROR')