import sys

sys.stdin = open('input.txt','r')
N = int(sys.stdin.readline())
# DP matrix의 정의는 DP[i][j]는 i에서 j까지의 

def solution(length,array):
    M=length
    DP=[[0]*(M) for i in range(M)]

    for k in range(0,M):
        for l in range(k,-1,-1):
            if l == k : continue
            
            DP[l][k] = min([DP[l][i] + DP[i+1][k] for i in range(l,k)]) + sum(array[l:k+1])
    return DP[0][M-1]

for i in range(N):
    para1 = int(sys.stdin.readline())
    para2=list(map(int,sys.stdin.readline().split()))
    print(solution(para1,para2))
