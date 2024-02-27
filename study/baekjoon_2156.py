n = int(input())
arr = []

for _ in range(n) : 
    arr.append(int(input()))

d = [0] * n
d[0] = arr[0]

if n > 1:
    d[1] = arr[0] + arr[1]

if n > 2:
    d[2] = max(d[1], arr[0]+arr[2], arr[2]+arr[1])

for i in range(3, n) : 
    d[i] = max(d[i-1], d[i-3]+arr[i]+arr[i-1], d[i-2]+arr[i])

print(d[n-1])
