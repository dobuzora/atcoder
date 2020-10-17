import math

def calc_manhattan(x):
    return sum(x)

def calc_euclidean(x):
    return math.sqrt(sum(map(lambda n : n**2, x)))

def calc_chebyshev(x):
    return max(x)

def convert_abs(x):
    return abs(int(x))

n = int(input())
x = list(map(lambda n : abs(int(n)), input().split()))
# x = list(map(int, input().split()))


print(calc_manhattan(x))
print(calc_euclidean(x))
print(calc_chebyshev(x))
