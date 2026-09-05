import math

n = int(input())
letters = input().split()
k = int(input())

total_a = letters.count('a')
not_a = n - total_a

total_combinations = math.comb(n, k)
no_a_combinations = math.comb(not_a, k) if not_a >= k else 0

probability = 1 - (no_a_combinations / total_combinations)

print(f"{probability:.4f}")
