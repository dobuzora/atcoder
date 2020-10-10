H, W = map(int, input().split())
table = str.maketrans({
    '.':'1',
    '#':'0'
})
S = [input().translate(table) for i in range(H)]

def calc_horizontal(text):
    count = 0
    for i, w in enumerate(text):
        wi = int(w)
        j = i + 1
        if j < len(text):
            wj = int(text[j])
            if (wi * wj) == 1:
                count += 1
    return count

def calc_vertical(text1, text2):
    count = 0
    for w1, w2 in zip(text1, text2):
        if (int(w1) * int(w2)) == 1:
            count += 1
    return count


result = 0
for i, Si in enumerate(S):
    result += calc_horizontal(Si)
    j = i + 1
    if j < H:
        Sj = S[j]
        result += calc_vertical(Si, Sj)
print(result)
        