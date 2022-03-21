def add_user(**user):
    print(user)


def print_user(**user):
    for key, value in user.items():
        print(f'{key} = {value}')

    
add_user(id=1, Name='John', Surname='Kowalski', Age=25)
print_user(id=1, Name='John', Surname='Kowalski', Age=25)
print("\n***\n")


def add_user(**user):
    users.append(user)


users = []
add_user(id=1, Name='John', Surname='Kowalski', Age=25)
add_user(id=2, Name='Jessica', Surname='Supergirl', Age=26)
print(users)