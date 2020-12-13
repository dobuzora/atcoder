from numpy.linalg import solve

s_x, s_y, g_x, g_y = tuple(map(int, input().split()))

left = [[s_x, 1],
        [g_x, 1]]

right = [-s_y, g_y]

a,b = solve(left, right)

print(-(b/a))

