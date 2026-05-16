def kio(n):
    value=0

    while value <= n:
        yield value
        
        value+=1

for m in kio(3):
    print(m)