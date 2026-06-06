from xml.sax.saxutils import escape

data=input('Enter Message: ')
flag='f'
escape='e'

stuffed= ' '

for ch in data:
    if ch==flag:
        stuffed +=escape
    stuffed+=ch
print(stuffed)