# あなたは、室温が 30度以上のとき、またそのときに限り、冷房の電源を入れます。今の室温は X度です。冷房の電源を入れますか？
# −40≤X≤40
# X は整数である。
X = int(input())
if not  X < -40  or 40 < X:
    if X >= 30:
        print("Yes")
    else:
        print("No")
else:
    print("No")