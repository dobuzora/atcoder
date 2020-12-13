N = int(input())
T = input()
import math



n = math.floor(N/3) # 3 == len('110')
i = 0
c = 0
ix1 = 0
ix2 = 0
while True:
   s = '110' * n
   # sの桁数がi++されない
#    ri = n % 3
#    s = s[]
   if s.count(T, i) == 1:
       c += 1
   if c == 1:
       ix1 = i
   if c == 2:
       print(s)
       ix2 = i
       break
   n += 1
   i += 1
print(ix1, ix2)