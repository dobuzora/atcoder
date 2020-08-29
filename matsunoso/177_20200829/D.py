N, M = map(int, input().split())
friend_realtions = []
for i in range(M):
    r1, r2 = map(int, input().split())
    friend_realtions.append([r1, r2])
print(friend_realtions)