import sys
input = sys.stdin.readline

stack = []
n = int(input())
result = []
now = 0

for i in range(1, n+1) :
    num = int(input())

    if now == 0 and len(stack) == 0 : #초기
        for j in range(num):
            stack.append(j+1)
            result.append("+")
            now = num
        result.append("-")
        stack.remove(num)

    elif now != 0 and len(stack) == 0 :
        for j in range(now+1, num+1) :
            result.append("+")
            stack.append(j)

        stack.remove(num)
        result.append("-")

        now = num

    elif len(stack)!= 0  and stack[-1] == num:
        stack.remove(num)
        result.append("-")

    elif len(stack)!= 0 and num > stack[-1] :
        for j in range(now+1, num+1) :
            result.append("+")
            stack.append(j)
            now = num
        stack.remove(num)
        result.append("-")

if len(stack) == 0 :
    for i in result:
        print(i)

else:
    print("NO")
    