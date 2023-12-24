import sys
input = sys.stdin.readline

stack = []
n = int(input())
result = []
now = 0

for i in range(1, n+1) :
    num = int(input())

    if now == 0 and len(stack) == 0 : # 가장 먼저 입력받은 숫자
        for j in range(num):
            stack.append(j+1)
            result.append("+")
            now = num
        result.append("-")
        stack.remove(num)

    # elif now != 0 and len(stack) == 0 : # 스택이 비었지만, 초기상태는 아닐 때
    #     for j in range(now+1, num+1) :
    #         result.append("+")
    #         stack.append(j)

    #     stack.remove(num)
    #     result.append("-")

    #     now = num

    elif len(stack)!= 0  and stack[-1] == num: # 입력받은 숫자와 스택의 top이 일치할 때
        stack.remove(num)
        result.append("-")

    # elif len(stack)!= 0 and num > stack[-1] : # 입력받은 숫자가 한번도 stack에 들어온 적 없었을 때
    #     for j in range(now+1, num+1) :
    #         result.append("+")
    #         stack.append(j)
    #         now = num
    #     stack.remove(num)
    #     result.append("-")/
    else:
        for j in range(now+1, num+1) :
            result.append("+")
            stack.append(j)
            now = num
        stack.remove(num)
        result.append("-")

if len(stack) == 0 : #스택이 비었을 때는 가능하다
    for i in result:
        print(i)

else: #스택에 숫자가 남아있을 경우는 불가능
    print("NO")
    