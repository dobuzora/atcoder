S = input()
T = input()

count = []
for i in range(len(S) - len(T) + 1):
    match_count = 0
    for s, t in zip(S[i:i+len(T)], T):
        if s in t:
            match_count += 1
    count.append(match_count)

print(len(T) - max(count))
            