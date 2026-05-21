import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    if re.search(pattern, ip):
       address = ip.split('.')
       for num in address:
           if int(num) > 255:
               return False
           if len(num)>1 and num.startswith('0'):
               return False
    return True
    return False






if __name__ == "__main__":
    main()
