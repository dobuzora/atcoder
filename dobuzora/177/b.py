s = list(input())
t = list(input())

roop_count = len(s) - len(t) + 1
score = -1

for i in range(roop_count):
    match = 0
    for j,v in enumerate(s[i:len(t)+i]):
        if t[j] == v:
            match += 1
    if match > score:
        score = match

print(len(t) - score)
