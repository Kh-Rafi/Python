import re

def replace_symbols(match):
    if match.group(0) == '&&':
        return 'and'
    else:
        return 'or'

n = int(input())

for _ in range(n):
    line = input()
    modified_line = re.sub(r'(?<= )(&&|\|\|)(?= )', replace_symbols, line)
    print(modified_line)
