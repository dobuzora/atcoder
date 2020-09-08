from collections import OrderedDict
N = int(input())
S = OrderedDict([('AC', 0), ('WA', 0), ('TLE', 0), ('RE', 0)])
for i in range(N):
    text = input()
    if text in S.keys():
        S[text] =S[text] + 1
        # print(S)

for key, value in S.items():
    print('{} x {}'.format(key, value))