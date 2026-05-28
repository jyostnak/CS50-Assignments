from datetime import date
import sys
import inflect
import re

def main():
    bday = input("Date of birth: ")
    print(convert(bday))


def convert(bday):
    p = inflect.engine()
    pattern = r"\d{4}-\d{2}-\d{2}"
    if not re.fullmatch(pattern, bday):
        sys.exit('Invalid date')
    year, month, date_ = bday.split('-')
    today = date.(2000, 1, 1)
    bdate = date(int(year), int(month), int(date_))
    diff = today - bdate
    days = diff.days
    number = days*24*60
    age = p.number_to_words(number, andword='')
    age = age.capitalize()
    return f'{age} minutes'

def print():
    print(main())


if __name__ == "__main__":
    main()
