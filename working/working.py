import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"[0-12]:?[0-6]?[0-9]? (AM)?(PM)? to [0-12]:?[0-6]?[0-9]? (AM)?(PM)?"


...


if __name__ == "__main__":
    main()
