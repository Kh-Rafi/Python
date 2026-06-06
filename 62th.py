data=input('Enter Message: ')

escape='e'

destuffed= ' '

i=0

while i<len(data):
    if data[i]==escape:
        i+=1
    destuffed+=data[i]
    i+=1
print(destuffed)