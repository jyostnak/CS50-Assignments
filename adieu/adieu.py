import inflect

engine = inflect.engine()
def makelist(name, n):
    n.append(name)
    return name

names = []

while True:
    try:
        name = input('Name: ')
        makelist(name, names)

    except EOFError:
        print()
        break

final = engine.join(names)
print(f'Adieu, adieu, to {final}')






