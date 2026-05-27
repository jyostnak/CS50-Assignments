from datetime import date
import sys
import inflect
import re


def main():
    p = inflect.engine()
    bday = input("Date of birth: ")
    pattern = r"\d{4}-\d{2}-\d{2}"
    if not re.fullmatch(pattern, bday):
        sys.exit('Invalid date')
    year, month, date_ = bday.split('-')
    today = date.today()
    bdate = date(int(year), int(month), int(date_))
    diff = today - bdate
    days = diff.days
    number = days*24*60
    return p.number_to_words(number, andword='')

def print():
    print(main())


if __name__ == "__main__":
    main()
