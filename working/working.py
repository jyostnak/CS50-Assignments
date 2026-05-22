import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d):?(\d)?(AM|PM) to (\d):?(\d)?(AM|PM)"
    if match := re.search(pattern, s):
        h1 = match.group(1)
        m1 = match.group(2)
        p1 = match.group(3)

        h2 = match.group(4)
        m2 = match.group(5)
        p2 = match.group(6)

        if m1>60 or m2>60:
            raise ValueError

        if m1 is None:
            m1 = '00'
        if m2 is None:
            m2 = '00'

        if h1>12 or h2>12:
            raise ValueError

        if p1 == 'PM':
            h1 = h1 + 12
        if p1 == 'AM':
            if h1 == '12':
                h1 = '00'
                
        if p2 == 'PM':
            h2 = h2 + 12
         if p2 == 'AM':
            if h2 == '12':
                h2 = '00'








...


if __name__ == "__main__":
    main()
