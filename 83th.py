import re

S = input().strip()
K = input().strip()

matches = list(re.finditer(r'(?={})'.format(re.escape(K)), S))

if matches:
    for match in matches:
        print(f"({match.start()}, {match.start() + len(K) - 1})")
else:
    print("(-1, -1)")
