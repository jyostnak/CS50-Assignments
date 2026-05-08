#jpg,jpeg,png,gif-->image
#pdf,zip-->app
#txt-->text/plain
name = input('File Name:')
name=name.strip().lower()
name=name.replace('.',' ')
name=name.split()
image = ['gif','jpg','jpeg','png']
app = ['pdf','zip']
if set(name) & set(image):
    b=list(set(name) & set(image))
    b=''.join(b)
    if b=='jpg' or b=='jpeg':
        print('image/jpeg')
    else:
        print("image/"+b)
elif set(name) & set(app):
    b=list(set(name) & set(app))
    b=''.join(b)
    print("application/"+b)
elif 'txt' in name:
    print('text/plain')
else:
    print("application/octet-stream")

