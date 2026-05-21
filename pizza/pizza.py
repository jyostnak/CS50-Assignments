import sys
from tabulate import tabulate
import csv

if len(sys.argv) <2:
    sys.exit("Too few command-line argument")
if len(sys.argv) > 2:
    sys.exit("Too many command=line arguments")
file_name = sys.argv[1]
if not file_name.endswith('.csv'):
    sys.exit("Not a csv file")

try:
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        table = tabulate(reader, headers="keys", tablefmt="grid")
        print(table)
except FileNotFoundError:
    sys.exit("File does not exist")



