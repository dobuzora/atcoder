# 高橋君は K の倍数と 7 が好きです。
# 7,77,777,… という数列の中に初めて K の倍数が登場するのは何項目ですか？
# 存在しない場合は代わりに -1 を出力してください。
# 制約
## 1≤K≤10^6
## K は整数である。

import math
K = int(input())

# 10^6とそれより1つ小さい777777まで7の配列を確保すれば良いのでは？
S = [int('7' * i) for i in range(1, math.floor(math.log((10 ** 6) * 77777, 10)))]
start = math.floor(math.log(K, 10))
count = [a for a in S[start:] if a % K == 0]
if len(count) == 0:
    print(-1)
else:
    print(len(str(count[0])))