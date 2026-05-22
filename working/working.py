import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d):?(\d)?(AM|PM) to (\d):?(\d)?(AM|PM)"
    if match := re.search(pattern, s):
        




...


if __name__ == "__main__":
    main()
