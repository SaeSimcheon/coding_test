# 그냥 피보나치 수열 문제임임
import sys
sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline())


def solution():

    F = [1,2]

    for i in range(2,N):
        F.append(F[i-1]+F[i-2])

    print(F[N-1]%10007)


    return 
solution()
