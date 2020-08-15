N = int(input())
L = list(map(int, input().split()))
L = sorted(list(set(L)))
# print(sorted(list(set(L))))

def triangle(v1, v2, v3):
    if (v1 + v2) > v3 and (v2 + v3) > v1 and (v3 + v1) > v2:
        return 1
    else:
        return 0

# # L(0)を固定し、L(1)を固定し、L(2)を選択する
result = 0

for v1 in L:
    l_1 = L[1:]
    for v2 in l_1:
        l_2 = L[2:]
        for v3 in l_2:
            if triangle(v1, v2, v3):
                result = result + 1

print(result)