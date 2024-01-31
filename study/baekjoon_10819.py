import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tmp = []
arr = sorted(arr)

t = n//2
j = 0

#개수가 짝수일 경우
if n%2 == 0 :
    for i in range(len(arr)//2) : 
      if tmp == 0:
         break

      if j % 2 == 0 : 
          tmp.insert(0, arr[(n//2)+t-1])
          tmp.append(arr[(n//2)-t])

      else : 
           tmp.insert(0,arr[(n//2)-t])
           tmp.append(arr[(n//2)+t-1])

      t-=1
      j+=1

else: # 개수가 홀수일 경우
    for i in range(len(arr)//2) : 
      if tmp == 0:
         break

      if j % 2 == 0 :
          tmp.insert(0, arr[(n//2)+t])
          tmp.append(arr[(n//2)-t])

      else : 
           tmp.insert(0,arr[(n//2)-t])
           tmp.append(arr[(n//2)+t])

      t-=1
      j+=1

    # 정렬 후 중간 index에 있는 숫자를 맨 뒤에 넣을지 앞에 넣을지 결정
    if abs(tmp[0] - arr[n//2]) > abs(tmp[len(tmp)-1] - arr[n//2]) :
        tmp.insert(0, arr[n//2])
    else:
        tmp.append(arr[n//2])


answer = 0
l, m = 0, 1
for i in range(len(tmp)-1) : #차례대로 계산 
    answer+=abs(tmp[l]-tmp[m])
    l+=1
    m+=1

print(answer)