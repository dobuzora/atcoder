N = int(input())
A = [int(x) for x in input().split()]

outer_sum = 0
for i in range(N-1):
    j = i + 1
    inner_sum = 0
    for k in range(j,N):
        inner_sum += A[i] * A[k]
    outer_sum += inner_sum

print(outer_sum % (10**9 + 7))