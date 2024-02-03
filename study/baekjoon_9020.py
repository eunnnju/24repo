import math
T = int(input())

def is_prime(num) :
    if num == 2: # 2는 소수
         return True

    for i in range(2, int(math.sqrt(num))+1) : 
        if num % i == 0 :
            return False
    return True

def solution(n) : 
    a, b = n//2, n//2 #a는 작아지고, b는 커질 것
    for i in range(1, (n//2)+1) :
        if is_prime(a) and is_prime(b):
                return a,b
        a-=1
        b+=1


for _ in range(T) : 
    n = int(input())

    print(*solution(n))

