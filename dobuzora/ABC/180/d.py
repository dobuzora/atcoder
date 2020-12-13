import math
x,y,a,b = map(int,input().split())

e = 0
while x <= y:
    if (x * a) < (b):
        x *= a
        e += 1
    else:
        e += (y - x) / b
        break
print(int(e))



