# 2 次元平面上に N 個の点があります。 i 個目の点の座標は (Xi,Yi) です。
# これらのうち、原点からの距離が D 以下であるような点は何個ありますか？
# なお、座標 (p,q) にある点と原点の距離は √(p2+q2) で表されます。
# 制約
## 1≤N≤2×10^5
## 0≤D≤2×10^5
## |Xi|,|Yi|≤2×10^5
## 入力は全て整数
import math

N, D = map(int, input().split())
P = []
for n in range(N):
    X_n, Y_n = map(int, input().split())
    P.append((X_n, Y_n))

def distance(p:tuple):
    return math.sqrt(p[0] ** 2 + p[1] ** 2)

count = [p for p in P if distance(p) <= D]
print(len(count))