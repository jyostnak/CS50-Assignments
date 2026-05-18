def main():
    a=input("Greetings:")
    greet = value(a)
    print(greet)

def value(greeting):
    a = greeting.strip().lower()
    a=a.replace(',','')
    a=a.split()
    b="".join(a)
    if 'hello' in a:
        return "$0"
    elif 'h' in b[0]:
        return '$20'
    else:
        return '$100'

if __name__ == '__main__':
    main()

