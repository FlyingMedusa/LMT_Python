'''
Marta Sleboda
Exercise 15
'''

def reading_file(filename):
    '''
    input: txt file
    output: a list of strings
    '''
    try:
        with open(filename, 'r') as f:
            lines = f.readlines() 
    except IOError as e:
        print(f'A file {filename} has not been found!\nThe full error message: {e}')
        return "error"
    except:
        print('Something went wrong...')
        return "error"
    if lines == []:
        print('The file seems to be empty!')
        return "error"
    return lines


def send(dict, total):
    '''
    input: dictionary(key: int of line_no, value: int), int
    output: txt file
    '''
    with open('summary.txt', 'w', encoding='utf-8') as f:
        for key in dict:
            f.write(f'There are {dict[key]} vowels in line no {key}.\n')
        f.write(f'There are totally {total} vowels.')
    print('A file summary.txt has been saved!')


def get_vowels_number(lines):
    '''
    input: a list of strings
    output: a dictionary: key - line number, value - number of vowels
    '''
    vowels_by_row = {}
    i = 1
    for line in lines:
        vowels_by_row[i] = 0
        for character in line:
            if character.lower() in 'aeiouy':
                vowels_by_row[i] += 1
        i += 1
    return vowels_by_row


def vowels_total(dict):
    '''
    input: dictionary(key: int of line_no, value: int)
    output: int - total number or vowels
    '''
    total_count = 0
    i = 1
    for _ in dict:
        total_count += dict[i]
        i += 1
    return total_count


def printing_selected(dict, end):
    '''
    input: dictionary(key: int of line_no, value: int), int (how many lines to print)
    '''
    counter = 0
    print(f'SNEAK PEEK - First {end} lines:')
    for key in dict:
        counter += 1
        if counter < end+1:
            print(f'There are {dict[key]} vowels in line no {key}.')
        else:
            break


def main():
    filename = 'shakespeare.txt'
    # reading
    lines = reading_file(filename)
    if lines == "error":
        exit()
    # cleaning
    lines = list(filter(lambda a_line: (a_line != '\n'), lines)) 
    # creating a dictionary [key: line num, value: vowel count]
    vowels_by_row = get_vowels_number(lines)
    # peeking into data
    printing_selected(vowels_by_row, 15)
    # printing total vowel count
    print(f'There are totally {vowels_total(vowels_by_row)} vowels.')
    # saving
    send(vowels_by_row, vowels_total(vowels_by_row))


if __name__ == "__main__":
    main()