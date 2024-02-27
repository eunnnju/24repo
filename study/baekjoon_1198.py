N = int(input())
graph = []

for _ in range(N) : 
    i,j = map(int,input().split())
    graph.append((j,i))

print(graph)