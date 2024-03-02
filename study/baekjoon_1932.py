n = int(input())
graph = []

for _ in range(n) : 
    graph.append(list(map(int, input().split())))

if n == 1:
    print(*graph[0])

else :
    graph[1][0] = graph[0][0] + graph[1][0] 
    graph[1][1] = graph[0][0] + graph[1][1]    


    for i in range (3, n+1) : 
        for j in range(i) :
            if j == 0:
                graph[i-1][j] = graph[i-2][0] + graph[i-1][j]

            elif j == i-1 :
                graph[i-1][j] = graph[i-2][i-2] + graph[i-1][j]

            else :
                graph[i-1][j] = max(graph[i-2][j-1], graph[i-2][j]) + graph[i-1][j]

    print(max(graph[n-1]))