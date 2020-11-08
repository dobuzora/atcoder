N = int(input())
A = list(map(int, input().split()))

score = 0
temp_score = 0
for i in range(len(A)+1):
    for a in A[:i]:
        temp_score += a
        if temp_score > score:
            score = temp_score
print(score)