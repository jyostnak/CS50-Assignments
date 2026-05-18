def convert(n):
    lst = []
    for ch in n:
        lst.append(ch)
    for i in range(len(lst)):
        if lst.count('/') != 1:
            break
        elif lst[i] == '/':
            before = int(''.join(lst[:i]))
            after = int(''.join(lst[i+1:]))
            result = (before/after)*100
            if result<0 or result>100:
                raise ValueError
            if before<0:
                raise ValueError
            if before > after:
                raise ValueError
    return result

def gauge(result):
    if 0<=result<=1:
        return "E"
    elif 99<=result<=100:
        return "F"
    else:
        return f'{round(result)}%'

def main():
    while True:
        try:
            result = convert(input('Fraction: '))
            final = gauge(result)
            print(final)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == '__main__':
    main()
