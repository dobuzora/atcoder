N, K = list(map(int, input().split()))
T = list()
for n in range(N):
    T.append(list(map(int, input().split())))

route_count = 0

def timeCalc(num_city):
    num_city = num_city - 1
    if num_city < 0:
        return 0
    
