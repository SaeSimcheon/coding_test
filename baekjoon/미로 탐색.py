
# 최단거리 문제
# queue는 선입선출이다.
import sys

sys.stdin = open('input.txt','r')

N,M=map(int,sys.stdin.readline().split())
mat=[list(sys.stdin.readline().rstrip()) for _ in range(N)]
DP = [[0]*M for _ in range(N)]
DP[0][0] =1

Q = [(0,0)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
mat[0][0]=1
while Q:
    x,y = Q.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny <M:    
            if mat[nx][ny] == '1':
                mat[nx][ny] = '0'
                DP[nx][ny] = DP[x][y]+1
                Q.append((nx,ny))
    

print(DP[N-1][M-1])



# 다른 사람은 어떻게 풀었을까 ?
# 큐. pop을 굳이 하지 않고 매번 임시로 큐를 만들어서 반복 시행이 종료될때 갱신.
# 즉, 반복이 큐의 원소 하나마다 일어나는 것이 아니라, level마다 일어나게 함.
# level count를 한 후에 원하는 좌표에 최초로 도착한 경우 break 하면 됨.
# 

from sys import stdin

n,m = map(int,input().split())

maze = [[0]*(m+2)]
for _ in range(n):
    maze.append([0]+list(map(int,list(stdin.readline().rstrip("\n"))))+[0])
maze.append([0]*(m+2))

que = [(1,1)]
maze[1][1] == 0
count = 1
while True:
    temp = []
    for node in que:
        i,j = node
        if maze[i+1][j] != 0:
            temp.append((i+1,j))
            maze[i+1][j] = 0

        if maze[i-1][j] != 0:
            temp.append((i-1,j))
            maze[i-1][j] = 0

        if maze[i][j+1] != 0:
            temp.append((i,j+1))
            maze[i][j+1] = 0

        if maze[i][j-1] != 0:
            temp.append((i,j-1))
            maze[i][j-1] = 0


    que = temp
    count += 1
    if (n,m) in temp:
        break

print(count)
        


# 

import sys
input = sys.stdin.readline

def BFS(start:tuple, end:tuple, size:tuple, arr:list):
    n,m = size
    queue = [start]
    move = [(-1,0),(1,0),(0,-1),(0,1)]
    cnt = 1
    while True:
        tmp = []
        for i,j in queue:
            arr[i][j]=0
            for di, dj in move:
                if 0 <= i + di < n and 0 <= j + dj < m and arr[i+di][j+dj]:
                    if (i+di,j+dj) == end:
                        print(cnt+1)
                        return 
                    tmp.append((i+di, j+dj))
                    arr[i+di][j+dj] = 0
        queue = tmp
        cnt+=1

def BOJ2178():
    n,m = map(int, input().split())
    maze = [[int(s) for s in input().split()[0]] for _ in range(n)]
    BFS(start=(0,0), end=(n-1,m-1), size=(n,m), arr=maze)
BOJ2178()
