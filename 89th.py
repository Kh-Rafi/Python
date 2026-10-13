import re
import email.utils
n = int(input())

pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for _ in range(n):
    line = input()

    parsed_name, parsed_email = email.utils.parseaddr(line)
    
    if re.match(pattern, parsed_email):
        print(line)