import re

s = input().strip()

vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"

pattern = rf'(?<=[{consonants}])[{vowels}]{{2,}}(?=[{consonants}])'

matches = re.findall(pattern, s, re.IGNORECASE)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)