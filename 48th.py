import re

pattern='^a...s$'
string="abbas"

result=re.match(pattern, string)

if result:
    print("Match")
else:
    print("Not Match.")