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

''' 
import sys
input = sys.stdin.readline


dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs_bound(bd, start, end):
    if start == end:
        return 0
    que = [start]
    visited = {start}
    m = 1
    while True:
        new_que = []
        for x, y in que:
            for i, j in zip(dx, dy):
                nx, ny = x+i, y+j
                if 0 <= nx < bd and 0 <= ny < bd:
                    new = nx, ny
                    if new not in visited:
                        visited.add(new)
                        new_que.append(new)
        if end in visited:
            return m
        m += 1
        que = new_que

def bfs(p):
    if p == (0, 0):
        return 0
    start = (0, 0)
    que = [start]
    visited = {start}
    for m in range(1, 10):
        new_que = []
        for x, y in que:
            for i, j in zip(dx, dy):
                new = x + i, y + j
                if new not in visited:
                    visited.add(new)
                    new_que.append(new)
        if p in visited:
            return m
        que = new_que

def manual(x, y):
    i = 0
    while x >= 5 or y >= 5:
        x, y = (x-2, abs(y-1)) if x > y else (abs(x-1), y-2)
        i += 1
    return i + bfs((x, y))

for _ in range(int(input())):
    bd = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x, y = abs(x1-x2), abs(y1-y2)
    if x >= 5 or y >= 5:
        print(manual(x, y))
    else:
        print(bfs_bound(bd, (x1, y1), (x2, y2)))
'''
