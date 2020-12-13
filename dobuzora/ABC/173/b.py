num = int(input())

count = {"AC":0,"WA":0,"TLE":0,"RE":0}

for _ in range(num):
    s = input()
    count[s] += 1

print("AC x {}".format(count["AC"]))
print("WA x {}".format(count["WA"]))
print("TLE x {}".format(count["TLE"]))
print("RE x {}".format(count["RE"]))
