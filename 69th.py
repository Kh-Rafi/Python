from collections import deque

d=deque()

n= int(input())
for i in range(n):
    parts= input().split()
    method = parts[0]
    
    if len(parts)>1:
        val = int(parts[1])
        getattr(d,method)(val)
    else:
        getattr(d,method)()

print(*(d))