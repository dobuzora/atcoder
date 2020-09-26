N, M = map(int, input().split())
A = []
B = []
for m in range(M):
    A[m], B[m] = map(int, input().split())
road = set(A) + set(B)
num = N -  M - len(road)
if not num < 0:
    print(num)