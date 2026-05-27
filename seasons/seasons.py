from datetime import date
import sys
import inflect
import re


def main():
    bday = input("Date of birth: ")
    pattern = r"\d{4}-\d{2}-\d{2}"
    match = re.search(pattern, bday)


...


if __name__ == "__main__":
    main()
