Sx, Sy, Gx, Gy = list(map(int, input().split()))
Tx = Sx + (Gx - Sx) * (abs(Sy) / abs(Sy + Gy))
# print(Sx)
# print(abs(Gx - Sx))
# print(Sy / Gy)
print(Tx)