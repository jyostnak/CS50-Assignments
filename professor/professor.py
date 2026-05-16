import random


def main():
    level = get_level()
    score = 0
    for i in range(10):

        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y

        for j in range(3):
            user_ans = input((f'{x} + {y} = '))
            if str(ans) == user_ans:
                score += 1
                break
            else:
                print('EEE')

                if j == 2:
                    print(f"{x} + {y} = {ans}")

    print(score)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            levels = [1,2,3]
            if level not in levels:
                raise ValueError
            break
        except ValueError:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x0 = random.randint(0, 9)
        return x0

    if level == 2:
        x1 = random.randint(10, 99)
        return x1

    if level == 3:
        x2 = random.randint(100, 999)
        return x2




if __name__ == "__main__":
    main()
