def main():

    word = input("Input:")
    print(f'Output: {shorten(word)}')

def shorten(word):

    input_list = []
    for ch in word:
        input_list.append(ch)
    i = 0
    vowels = ['a','e','i','o','u']
    while i<len(input_list):
        if input_list[i].lower() in vowels:
            input_list.pop(i)

        else:
            i+=1
    output = ''.join(input_list)
    return output

if __name__ == '__main__':
    main()


