#Enter tyour expression with space between the number and operation.
a=input("Expression:")
a=a.split()
if '+' in a:
    b = int(a[0])+int(a[2])
    b = float(b)
    b = round(b,1)
    print(b)
if '-' in a:
    b = int(a[0])-int(a[2])
    b = float(b)
    b = round(b,1)
    print(b)
if '*' in a:
    b = int(a[0])*int(a[2])
    b = float(b)
    b = round(b,1)
    print(b)
if '/' in a:
    b = int(a[0])/int(a[2])
    b = float(b)
    b = round(b,1)
    print(b)
