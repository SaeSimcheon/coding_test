
# 더할 수 있는 수만큼 예외 항이 생겼었고, 
import sys
sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) for _ in range(N)]

def solution():
    end=max(data)

    F = [1,2,4]

    for i in range(3,end):
        F.append(F[i-1]+F[i-2]+F[i-3])
    
    for i in data:
        print(F[i-1])

    return 


solution()
