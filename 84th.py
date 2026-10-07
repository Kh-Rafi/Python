import re

t = int(input())

for _ in range(t):
    n = input()
    
    match = re.match(r'^[+-]?[0-9]*\.[0-9]+$', n)
    
    print(bool(match))