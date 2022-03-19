# 3차원으로 풀었어야함. https://jshong1125.tistory.com/31

from collections import deque 
dx = [1, -1, 0, 0] 
dy = [0, 0, -1, 1] 
def bfs(): 
    q = deque() 
    q.append([0, 0, 1]) 
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] 
    visited[0][0][1] = 1 
    while q: 
        x, y, c = q.popleft() 
        if x == n-1 and y == m-1: 
            return visited[x][y][c] 
        for i in range(4): 
            tx = dx[i] + x 
            ty = dy[i] + y 
            
            if 0 <= tx < n and 0 <= ty < m: 
                if a[tx][ty] == '1' and c == 1: 
                    
                    visited[tx][ty][0] = visited[x][y][1] + 1 
                    q.append([tx, ty, 0]) 
                    
                elif a[tx][ty] == '0' and visited[tx][ty][c] == 0: 
                    visited[tx][ty][c] = visited[x][y][c] + 1 
                    q.append([tx, ty, c]) 
    return -1 
n, m = map(int, input().split()) 
a = [] 
for i in range(n): 
    a.append(list(input())) 
    
print(bfs())






# 시간 초과
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




# 다른 사람 풀이

import sys

input = sys.stdin.readline


def sol2206():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    nw = {'0', '2'}
    q = [(0, 0, 2)]
    answer = 1
    while q:
        nq = []
        for r, c, w in q:
            if r == n - 1 and c == m - 1:
                return answer
            
            for nr, nc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc]!='3':
                    if w == 1:
                        if board[nr][nc] == '0':
                            board[nr][nc] = '2'
                            nq.append((nr, nc, 1))
                    else:
                        if board[nr][nc] == '1':
                            nq.append((nr, nc, 1))
                        elif board[nr][nc] in nw:
                            nq.append((nr, nc, 2))
                        board[nr][nc] = '3'
        answer += 1
        q = nq
    return -1


if __name__ == '__main__':
    print(sol2206())

