H, W = list(map(int, input().split(" ")))
A = []
for h in range(H):
    A.append(list(map(int, input().split(" "))))


for i, a in enumerate(A):
    if i == 0:
        a_min = min(a)
    else:
        if a_min > min(a):
            a_min = min(a)

count = 0
for a in A:
    for elm in a:
        # print(elm)
        count += (elm - a_min)
        # print(count)

# print(a_min)
print(count)