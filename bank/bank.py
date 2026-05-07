a=input("Greetings:")
a = a.strip().lower()
a=a.replace(',','')
a=a.split()
b="".join(a)
if 'hello' in a:
    print("$0")
elif 'h' in b:
    print('$20')
else:
    print('$100')
