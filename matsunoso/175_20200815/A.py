# input = S or R
# check S(R) and S(R→R)


S = input()
table = {
    'S':'0',
    'R':'1'
}
b_S = ''.join(table.get(c, c) for c in S)

r_1 = 0
r_2 = 0
result = 0
for s in b_S:
# 連続フラグ
    if int(s) == 1 and r_1 == 1:
        r_2 = 1
    else:
        r_2 = 0
# 1出現フラグ
    if int(s) == 1:
        r_1 = 1
    else:
        r_1 = 0
# 結果を更新
    if r_2 == 1:
        result = result + 1

# '1'が出現していれば1を追加する
if '1' in b_S:
    result = result + 1
print(result)