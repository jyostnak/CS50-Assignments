import csv
import sys

if len(sys.argv) <3:
    sys.exit("Too few command-line argument")
if len(sys.argv) > 3:
    sys.exit("Too many command=line arguments")
input_name = sys.argv[1]
output_name = sys.argv[2]
try:
    with open(input_name, 'r') as before, open(output_name, 'w') as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames = ["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            name = row["name"]
            name_lst = name.split(', ')
            second_name = name_lst[0]
            first_name = name_lst[1]
            writer.writerow({"first" : first_name,
                "last" : second_name,
                "house" : row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


