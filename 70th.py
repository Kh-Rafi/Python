from itertools import groupby

s = input().strip()
compressed = []

for character, group in groupby(s):
    count = len(list(group))
    compressed.append(f"({count}, {int(character)})")

print(" ".join(compressed))
