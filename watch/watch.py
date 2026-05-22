import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern  = r'^<iframe src="https?://(www\.)?youtube\.com/embed/(.+)"'
    if match := re.search(pattern, s):
        return f"https://youtu.be/{match.group(2)}"
    else:
        return None



if __name__ == "__main__":
    main()
