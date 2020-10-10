N = input()
p = list(map(int, input().split()))
for i in range(len(p)):
    p_original = set(p[:i+1])
    x = set(range(max(p[:i+1])))
    print(p_original)
    print(x)
    dif = x - p_original
    print(min(dif))