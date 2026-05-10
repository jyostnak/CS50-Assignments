camelFont = input('camelCase:')
camelList = []
for char in camelFont:
    camelList.append(char)
i = 0
while i<len(camelList):
    if 'A'<=camelList[i]<='Z':
        camelList.insert(i,'_')
        i+=1
    i+=1
snake_case = ''.join(camelList)
snake_case = snake_case.lower()
print(snake_case)

