import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError

    h1 = int(match.group(1))
    m1 = (match.group(2))
    p1 = match.group(3)

    h2 = int(match.group(4))
    m2 = (match.group(5))
    p2 = match.group(6)

    if m1 is None:
        m1 = '00'
    if m2 is None:
        m2 = '00'

    if int(m1)>60 or int(m2)>60:
        raise ValueError

    if h1>12 or h2>12:
        raise ValueError

    if p1 == "AM":
        if h1 == 12:
            h1 = 0
    else:
        if h1 != 12:
            h1 += 12

    if p2 == "AM":
        if h2 == 12:
            h2 = 0
    else:
        if h2 != 12:
            h2 += 12

    return f"{h1:02}:{m1} to {h2:02}:{m2}"



if __name__ == "__main__":
    main()
