import re

n = int(input())
inside_block = False

for _ in range(n):
    line = input()
    
    if '{' in line:
        inside_block = True
    elif '}' in line:
        inside_block = False
    elif inside_block:
        matches = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}\b', line)
        for match in matches:
            print(match)
