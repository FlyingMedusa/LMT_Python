'''
Marta Sleboda
'''

def slow_adding(num, j):
    ''' checks the cube root possibilities up to two decimal places'''
    curr_value = round(j + 0.01,2)
    curr_value_checker = curr_value**3
    if curr_value_checker == num:
        return curr_value
    elif curr_value_checker < num:
        return slow_adding(num, curr_value)
    else:
        back_in_time = round(curr_value - 0.01,2)
        return back_in_time


def my_cube_rooter(num):
    ''' calculates a cube root of an integer number using a loop '''
    for i in range(0,abs(num+1)):
        checker = i**3
        if checker == abs(num):
            if num >= 0:
                print(f"The cube root of {num} equals: {i}")
            else:
                print(f"The cube root of {num} equals: {-i}")
            break
        elif checker > abs(num):
            lower_i = i - 1
            if num >= 0:
                print(f"The cube root of {num} equals: {slow_adding(abs(num), lower_i)}")
            else:
                outcome = slow_adding(abs(num), lower_i)
                print(f"The cube root of {num} equals: {-outcome}")
            break


def main():
    print("Welcome to a program that calculates a cube root of an integer number using a loop.")
    while True:
        choice = input("Please enter a number.\nIf you want to leave the program, enter 'end'.\n")
        if choice == 'end':
            break
        else:
            try:
                choice = int(choice)
                my_cube_rooter(choice)
            except ValueError:
                print("<!> Enter an INTEGER or 'end' the program. <!>")


if __name__ == "__main__":
    main()