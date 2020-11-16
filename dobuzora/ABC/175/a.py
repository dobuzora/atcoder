a = input()
if a == 'RRR':
    print("3")
elif a == 'RRS' or a == 'SRR':
    print("2")
elif a == 'RSS' or a == 'RSR' or a == 'SSR' or a == 'SRS':
    print("1")
else :
    print("0")
