import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"https?://(www.)?youtube\.com/embed/.+"
    if match := re.search(pattern, s):
        link = re.sub(r"(www.)?/embed", "", match)
        return link
    return None




if __name__ == "__main__":
    main()
