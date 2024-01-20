import sys
from collections import deque
input = sys.stdin.readline

n, m, v =map(int, input().split())
graph = [[] for _ in range(n+1)]

dfs_list = []
bfs_list = []

for _ in range(m): # 그래프 생성
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
    
for i in range(len(graph)) : # 그래프 내부 정렬
    graph[i] = sorted(graph[i])

def bfs(v) :
    visited = [False]*(n+1)

    queue = deque()

    queue.append(v)
    bfs_list.append(v)

    while queue:
        l = queue.popleft()
        visited[l] = True

        for k in graph[l] :

            if visited[k] == False:
                visited[k] = True
                queue.append(k)
                bfs_list.append(k)
            
visited_dfs = [False] * (n+1)

def dfs(v) :
    visited_dfs[v] = True 
    dfs_list.append(v)

    for i in graph[v] :
        if not visited_dfs[i] : 
            dfs(i)

dfs(v)
print(*dfs_list)

bfs(v)
print(*bfs_list)