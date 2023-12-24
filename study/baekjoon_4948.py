import sys
import math #제곱근 계산
input = sys.stdin.readline

def is_prime_num(num):
    for i in range(2, int(math.sqrt(num))+1) :
        if num%i == 0 :
            return False
    return True

while True:
    m = int(input())

    if m == 0 :
        break

    else:
        ans = 0
        for num in range(m+1, 2*m+1) :
            if is_prime_num(num):
                ans += 1
    
    print(ans)