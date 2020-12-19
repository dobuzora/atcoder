from itertools import combinations
N = int(input())
A = list(map(int, input().split(" ")))

comb = list(combinations(A, 2))
result = sum([abs(a - b) for (a, b) in comb])
print(result)