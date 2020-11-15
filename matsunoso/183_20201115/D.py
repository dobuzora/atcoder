N, W = list(map(int, input().split()))
table = list()
for n in range(N):
    table.append(list(map(int, input().split())))
t_max = max([Tn[1] for Tn in table])
table = table.sort(key=lambda t:t[1])
