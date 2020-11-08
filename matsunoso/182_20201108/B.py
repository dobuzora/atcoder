N = int(input())
A = list(map(int, input().split()))
import math
A_max = max(A)
A_min = 2
max_gcd_num = 0
gcd_score = 0

for i in range(A_min, A_max+1):
    # print(i)
    temp_gcd_score = 0
    for a in A:
        if (a % i) == 0:
            temp_gcd_score += 1
    if temp_gcd_score >= gcd_score:
        max_gcd_num = i
        gcd_score = temp_gcd_score
    # print(temp_gcd_score)
print(max_gcd_num)