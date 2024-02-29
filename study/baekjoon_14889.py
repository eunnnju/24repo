from itertools import combinations, permutations
import math

N = int(input())
nums = [(i+1) for i in range(N)]

c = (math.factorial(len(nums))) / ((math.factorial(len(nums)//2)) * (math.factorial(len(nums)//2)) * 2) # 구해야 하는 경우의 수
cnt = 0

graph =[list(map(int ,input().split())) for _ in range(N)]

answer = [] #능력치 차이를 저장해둘 리스트

for i in combinations(nums, len(nums)//2) : 
    if cnt == c : 
        break

    tmp_a = 0
    tmp_b = 0
    a = list(i)
    b = [x for x in nums if x not in list(i)] # nums에서 a요소를 제외한 리스트

    for j in permutations(a, 2) :

        tmp_a += graph[j[0]-1][j[1]-1] + graph[j[1]-1][j[0]-1]


    for j in permutations(b, 2) :

        tmp_b += graph[j[0]-1][j[1]-1] + graph[j[1]-1][j[0]-1]

    answer.append(abs(tmp_a - tmp_b))    

    cnt+=1

print(min(answer)//2)
