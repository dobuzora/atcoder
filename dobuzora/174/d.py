def line_check(line, count):
    print(line)
    try:
        first_w = line.index("W")
    except:
        return count
    try:
        next_r_from_last = len(v_a) - list(reversed(v_a)).index("R") - 1
    except:
        return count
    if next_r_from_last > first_w:
        line[first_w], line[next_r_from_last] = line[next_r_from_last], line[first_w]
        count += 1
        return line_check(line, count)
    else :
        return count

_ = input()
v = input()
# v = "WWRWWRWWRR"
v_a = [str(i) for i in v]
a = line_check(v_a, 0)
print(a)



