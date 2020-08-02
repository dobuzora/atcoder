import math

n,d = map(int, input().split())

count = 0
for _ in range(n):
    x,y = map(int, input().split())
    dis = math.sqrt((x*x) + (y*y))
    if dis <= d:
        count += 1

print(count)
