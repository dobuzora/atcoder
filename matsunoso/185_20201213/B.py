N, M, T = list(map(int, input().split(' ')))
A = [None for i in range(M)]
B = [None for i in range(M)]

for i in range(M):
    A[i], B[i] = list(map(int, input().split(' ')))
A = [(2 * a) for a in A]
B = [(2 * b) for b in B]

# 初期値
battery = N
# flag = 0
# for t in range(2*T+1):
#     # 休憩かどうか確かめる
#     if t in A:
#         idx = A.index(t)
#         start, end = A[idx], B[idx]
#         flag = end # flagに次の休憩終わりを記録する
#     if t % 2 == 1:
#         # 充電
#         if t < flag:
#             if battery != N: # フル充電でない場合
#                 battery += 1
#         # 消耗
#         else:
#             if battery <= 0: # 空の場合、breakする
#                 break
#             else:
#                 battery -= 1
#     # print(f't={t}: バッテリー残量: {battery}')
# if battery > 0:
#     print('Yes')
# else:
#     print('No')

t_list = [None for t in range(2*T)]
for (a, b) in zip(A, B):
    # print(a, b)
    t_list[a:b] = [1 for i in range(len(t_list[a:b]))]
# print(t_list)
for i, t in enumerate(t_list):
    if i % 2 == 1:
        # 充電
        if t:
            if battery != N:
                battery += 1
        else:
            if battery <= 0:
                break
            else:
                battery -= 1
if battery > 0:
    print('Yes')
else:
    print('No')