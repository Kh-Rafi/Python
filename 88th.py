import re

n = int(input())

for _ in range(n):
    phone_number = input().strip()
    
    if re.match(r'^[789]\d{9}$', phone_number):
        print("YES")
    else:
        print("NO")
