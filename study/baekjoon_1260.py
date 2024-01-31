n = input()
line_tmp = sorted(n)
tmp = ''.join(map(str,line_tmp))
tmp = int(tmp)

flag = 0
for i in reversed(range(len(line_tmp))) :
    if tmp > int(n) :
        flag = 1
        break

    else:
        line_tmp[i-1], line_tmp[i] = line_tmp[i], line_tmp[i-1]
        tmp = ''.join(map(str, line_tmp))
        tmp = int(tmp)
        print(tmp)

if flag == 0:
    print(0)
else:
    print(tmp)