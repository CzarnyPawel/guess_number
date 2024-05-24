from random import randint
"""Simple game. The computer draw number. After then user  provides his number. Computer must compare this numbers."""

rnd = randint(1, 100)

while True:
    number = input('Guess the number: ')
    try:
        user_number = int(number)

    except ValueError:
        print("It's not a number!")
        continue
    if user_number < rnd:
        print('Too small!')
    elif user_number > rnd:
        print('Too big!')
    else:
        print('You win!')
        break
