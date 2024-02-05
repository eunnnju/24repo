import sys

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [None for _ in range(N+1)]

def dfs(graph, num, visited) : 
    # print("현재: ", num, graph[num], visited)

    for i in graph[num] : 
        if not visited[i] : 
            visited[i] = num
            dfs(graph, i, visited)

for _ in range(N-1) : 
    i,j = map(int ,input().split())
    graph[i].append(j)
    graph[j].append(i)

dfs(graph, 1, parent)

for i in range(2, N+1) : 
    print(parent[i])