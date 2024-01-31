import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tmp = []
arr = sorted(arr)

# 중간부터 채우자

t = n//2
j = 0
for i in range(len(arr)//2) : 
    if tmp == 0:
        break
    # print((n//2)+t-1, (n//2)-t)

    if j % 2 == 0 :
        tmp.insert(0, arr[(n//2)+t-1])
        tmp.append(arr[(n//2)-t])

    else : 
        tmp.insert(0,arr[(n//2)-t])
        tmp.append(arr[(n//2)+t-1])

    t-=1
    j+=1

answer = 0
l, m = 0, 1
for i in range(len(tmp)-1) : 
    answer+=abs(tmp[l]-tmp[m])
    l+=1
    m+=1

print(tmp)
print(answer)