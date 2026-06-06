data=input('Enter the stuffed data: ')

count=0
destuffed = " "

i=0

while i<len(data):
    destuffed+=data[i]

    if data[i]=="1":
        count+=1
    else:
        count=0
    if count==5:
        i+=1
        count=0
    i+=1
print(destuffed)