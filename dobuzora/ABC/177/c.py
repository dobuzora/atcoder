n = int(input())
nums = list(map(int, input().split()))

sum_value = 0
for i in range(n-1):
    for j in range(i+1,n):
        sum_value += nums[i]*nums[j]

print(sum_value%1000000007)
