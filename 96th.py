import re

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input())

decoded_string = ""
for j in range(m):
    for i in range(n):
        decoded_string += matrix[i][j]


result = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_string)

print(result)
