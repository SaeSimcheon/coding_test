# topdown 방식
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

# bottom up 방식

import sys
sys.stdin = open('input.txt','r')
read = lambda: sys.stdin.readline().strip()
from heapq import heappush, heappop

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(x, y):
    q = [(-arr[x][y], x, y)]                # 우선순위큐 사용, 높은 곳 부터 방문하도록
    dp = [[0] * m for _ in range(n)]        # 그래야 중복방문 할 때 올바르게 갱신됨
    dp[x][y] = 1

    while q:
        print(dp)
        cnt, cx, cy = heappop(q)
        print(f"cnt,cx,cy: {cnt},{cx},{cy}")
        print(f"q: {q}")
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if not 0 <= nx < n or not 0 <= ny < m:
                continue
            if arr[nx][ny] >= arr[cx][cy]:
                continue

            if dp[nx][ny] == 0:
                heappush(q, (-arr[nx][ny], nx, ny))
            dp[nx][ny] += dp[cx][cy]

    return dp


n, m = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(n)]

print(bfs(0, 0)[n - 1][m - 1])
