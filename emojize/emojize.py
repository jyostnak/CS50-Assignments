import emoji

input_ = input("Input: ")

emoj = emoji.emojize(input_)

if emoj == input_:
    emoj = emoji.emojize(input_, language='alias')

print(f'Output: {emoj}')
