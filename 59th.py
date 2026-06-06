data = input('Enter Binary Data: ')
count=0
stuffed=" "

for bit in data:
    stuffed+=bit

    if bit =='1':
        count+=1
    else:
        count=0
    if count==5:
        stuffed+='0'
        count=0

print('Stuffed Data:', stuffed)