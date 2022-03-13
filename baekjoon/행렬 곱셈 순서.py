import sys

sys.stdin = open('input.txt','r')
N = int(sys.stdin.readline())

data=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]



DP = [[0]*N for _ in range(N)]



for i in range(0,N):
    for j in range(i,-1,-1):
        if i == j : continue
        DP[j][i] = min([DP[j][k]+DP[k+1][i] + data[j][0]*data[k+1][0]*data[i][1] for k in range(j,i)])  
        # 행렬 비용 발생이 j번째 데이터의 row 차원 * k+1번째 행렬의 row 또는 k번째 행렬의 column 차원 * i번째 행렬의 column 차원
        # 11066번과 달리 cost가 k에 종속한다.
print(DP[0][N-1])
