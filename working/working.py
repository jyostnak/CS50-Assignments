import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d):?(\d)?(AM|PM) to (\d):?(\d)?(AM|PM)"
    if match := re.search(pattern, s):
        if int(match.group(1))>12 or int(match.group(4))>12:
            raise ValueError
        if match.group(2)>60 or int(match.group(5))>60:
            raise ValueError
        if match.group(3) == 'PM':
            hr = int(match.group(1)) + 12
        if match.group(6) == 'PM':
            hr_ = int(match.group(4)) + 12




...


if __name__ == "__main__":
    main()
