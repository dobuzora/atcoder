payment = int(input())
num = int(payment//1000)
if payment%1000 != 0:
    num += 1
    

print((num*1000)-payment)
