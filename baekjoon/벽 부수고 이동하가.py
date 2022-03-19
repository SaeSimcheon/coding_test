# 시간 초과과
import sys
from collections import deque
sys.stdin = open("input.txt",'r')

N,M=map(int,sys.stdin.readline().split())

mat = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

DP = [[0]*M for _ in range(N)]
    
y = [row[:] for row in DP]

D = [(1,0),(0,1),(-1,0),(0,-1)]
DP[0][0]=1
walls = deque([''])

for i in range(N):
    for j in range(M):
        if mat[i][j] == '1':
            walls.append((i,j))



def bfs(wall,matrix,DP_mat):
    
    
    if wall == '':
        pass
    else:
        matrix[wall[0]][wall[1]] = '0'
    
    Q = deque([(0,0)])
    while Q:
        x,y=Q.popleft()
        if x == N-1 and y == M-1:
            break
        for d in D :
            nx = x + d[0]
            ny = y + d[1]
            if 0<= nx < N and 0 <=ny < M and not DP_mat[nx][ny]:
                if matrix[nx][ny] == '0':
                    matrix[nx][ny] = '1'
                    DP_mat[nx][ny] = DP_mat[x][y] +1
                    Q.append((nx,ny))
    #print(DP_mat)
    if DP_mat[N-1][M-1] == 0:
        return -1
    else:
        return DP_mat[N-1][M-1]

result = float("inf")


for w in walls :
    this=bfs(w,[row1[:] for row1 in mat],[row2[:] for row2 in DP])
    #print(mat,DP)
    if result == float("inf"):
        result = this
    else:
        if result > this and this !=-1:
            result = this
        if result == -1:
            result = this
print(result)
