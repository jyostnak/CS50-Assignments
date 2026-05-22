import re
import sys
import validators

email = input("What's your email address? ")
pattern = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
if match := re.search(pattern, email):
    if validators.email(email):
            print("Valid")
    else:
            print("Invalid")
