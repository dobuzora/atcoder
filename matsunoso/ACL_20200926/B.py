A, B, C, D = map(int, input().split())
# 考えるべきは次の4通り
# A < C < B < D
# A < C < D < B
# C < A < B < D
# C < A < D < B
if A < C:
    if B >= C: # A < C < B
        print("Yes")
    else: # A < B < C
        print("No")
elif A > C:
    if A <= D: # C < A < D
        print("Yes")
    else: # C < D < A
        print("No")
else: # A == C
    print("Yes")
