import math
import sys

N = int(input())
n5 = math.ceil(math.log(N, 5))
n3 = math.ceil(math.log(N, 3)) 

for ni3 in range(n3):
    for ni5 in range(n5):
        temp = 3 ** ni3 + 5 ** ni5
        if temp == N:
            print(ni3, ni5)
            sys.exit()
    # if ni5 == n5 - 1:
    #     print(-1)
print(-1)