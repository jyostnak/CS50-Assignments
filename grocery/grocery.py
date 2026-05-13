def makedict(itemdict, n):
    if n in itemdict:
        itemdict[n] += 1
    else:
        itemdict[n] = 1

dicti = {}

while True:
    try:
        item = input()
        item = item.upper()
        makedict(dicti, item)
    except EOFError:
        break

for key, value in dicti.items():
    print(value, key)
