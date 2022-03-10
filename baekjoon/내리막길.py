import sys
sys.setrecursionlimit(10000) 
sys.stdin = open('input.txt','r')

N,M = map(int,sys.stdin.readline().split())


data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
check = [[-1]*M for _ in range(N)]


dx = [1,0,-1,0]
dy = [0,1,0, -1]

def dfs(x,y):
    if x == N-1 and y == M-1:
        return 1
    if check[x][y] !=-1:
        return check[x][y]
    
    check[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <=ny < M :
            if data[nx][ny] < data[x][y]:
                check[x][y] += dfs(nx,ny)
    return check[x][y]

print(dfs(0,0))

