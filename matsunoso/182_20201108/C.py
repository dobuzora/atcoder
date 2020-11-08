import sys
N = input()
K = len(N)

for k in range(0, K):
    for i in range(1,10):
        temp = N.replace(str(i), '', k)
        if (int(temp) % 3) == 0:
            print(k)
            sys.exit()
print(-1)
