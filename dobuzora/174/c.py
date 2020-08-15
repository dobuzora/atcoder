# def cycle(v,n):
#     n_str = str(n)
#     n_str += "7"
#     n = int(n_str)
#     if n % v == 0:
#         return len(n_str)
#     else :
#         return cycle(v,n)

def search_initial(v):
    seven_str = "7"
    while int(seven_str) < v:
        seven_str += "7"
    return int(seven_str)

k = int(input())

if k % 2 == 0:
    print("-1")
else :
    v = search_initial(k)
    while v % k != 0:
        v_str = str(v) + "7"
        v = int(v_str)
        print(v)
    print(v)


