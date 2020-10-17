import math
N = int(input())
X = list(map(int, input().split()))
manhattan_distance = sum([abs(xi) for xi in X])
euclid_distance = math.sqrt(sum([abs(xi)**2 for xi in X]))
cheby_chef_distance = max([abs(xi) for xi in X])

print(manhattan_distance)
print('{:.10f}'.format(euclid_distance))
print(cheby_chef_distance)