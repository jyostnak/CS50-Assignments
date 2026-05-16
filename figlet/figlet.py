import sys
from pyfiglet import Figlet
import random
figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) == 1:
    phrase = input('Input: ')
    len0 = random.choice(fonts)
    print(figlet.renderText(phrase))

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in fonts:
            phrase_ = input('Input: ')
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(phrase_))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

if len(sys.argv) == 2:
    sys.exit("Invalid usage")



