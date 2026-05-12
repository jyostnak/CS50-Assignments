def convert(n):
    lst = []
    for ch in n:
        lst.append(ch)
    for i in range(len(lst)):
        if lst[i] == '/':
            before = int(''.join(lst[:i]))
            after = int(''.join(lst[i+1:]))
            result = (before/after)*100
            if result<0 or result>100:
                raise ValueError
            if before<0:
                raise ValueError
            if before > after:
                raise ValueError
            if n.count('/') != 1:
                raise ValueError
    if 0<=result<=1:
        print('E')
    elif 99<=result<=100:
        print('F')
    else:
        print(f'{round(result)}%')

while True:
    try:
        convert(input('Fraction: '))
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

