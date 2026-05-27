from datetime import date
import sys
import inflect
import re


def main():
    bday = input("Date of birth: ")
    pattern = r"\d{4}-\d{2}-\d{2}"
    if not re.fullmatch(pattern, bday):
        sys.exit('Invalid date')
    year, month, date_ = bday.split('-')
    today = date.today()
    curr_year = today.year
    

...


if __name__ == "__main__":
    main()
