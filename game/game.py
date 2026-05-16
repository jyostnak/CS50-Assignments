import random

while True:
    try:
        level = int(input("Level: "))

        if level < 1:
            raise ValueError

        break

    except ValueError:
        pass

n = random.randint(1,level)

while True:
    try:
        m = input('Guess: ')
        m = int(m)
        if m < 1:
            raise ValueError
        if n == m:
            print('Just right!')
            break
        elif m > n:
            print('Too large!')
        elif m < n:
            print('Too small!')
    except ValueError:
        pass





