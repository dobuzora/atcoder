A, B, C = list(map(int, input().split()))
# sum = 0
# for a in range(1, A+1):
#     for b in range(1, B+1):
#         for c in range(1, C+1):
#             sum += a * b * c
def addUp(num):
    return  num * (num + 1) / 2
sum = addUp(A) * addUp(B) * addUp(C)
dev = 998244353
print(int(sum % dev))