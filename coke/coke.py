Amount = 50
while True:
    if Amount>0:
        print('Amount due =',Amount)
        given = int(input('Insert coin = '))
        Amount -= given
    else:
        print('Change owed =', -Amount)
        break
