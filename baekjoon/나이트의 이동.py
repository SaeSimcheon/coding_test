# 쉽게 풀긴 했는데 시간이 오래 걸림
'''
40689107	seob10278	7562	맞았습니다!!	33152	1944	Python 3 / 수정	760	50초 전
'''
import sys

sys.stdin = open("input.txt",'r')


N=int(sys.stdin.readline())

def bfs(I,p1,p2):
    DP = [[0]*I for _ in range(I)]
    

    D = [(2,1),(1,2),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
    from collections import deque
    Q = deque([p1])
    while Q :
        x,y=Q.popleft()
        if x == p2[0] and y == p2[1]:
            break
        for d in D:
            nx = x + d[0]
            ny = y + d[1]
            if 0<= nx < I and 0<=ny < I and not DP[nx][ny]:
                DP[nx][ny] = DP[x][y] +1
                Q.append((nx,ny))
    print(DP[p2[0]][p2[1]])

for i in range(N):
    I = int(sys.stdin.readline())
    p1=tuple(map(int,sys.stdin.readline().split()))
    p2=tuple(map(int,sys.stdin.readline().split()))
    bfs(I,p1,p2)
