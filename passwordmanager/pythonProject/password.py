import random as r

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '*', '&', '+', '-']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

selections = ['l', 's', 'n']


def generate_password():
    pswd = []

    for i in range(r.randrange(9, 12)):
        choice = r.choice(selections)
        if r.choice(choice) == "l":
            pswd.append(r.choice(letters))


        elif r.choice(choice) == 's':
            pswd.append(r.choice(symbols))

        elif r.choice(choice) == 'n':
            pswd.append(r.choice(numbers))




    pswd = ''.join(pswd)

    return pswd