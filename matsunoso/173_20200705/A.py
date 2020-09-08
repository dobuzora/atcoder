cost = input()
cost = int(cost)
div, mod = divmod(cost, 1000)
if mod == 0:
    bills = div
    change = 0
else:
    bills = div + 1
    change = 1000 - mod
print(change)