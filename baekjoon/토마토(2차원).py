# while의 한 단위를 level로 둔다. 
# Q에서 pop하지 않고 for을 사용하였으며 tmp를 따로두어 대입하는 방식을 사용했다.

import sys
sys.stdin = open('input.txt','r')

M,N=map(int,sys.stdin.readline().split())
data=[sys.stdin.readline().split() for _ in range(N)]
D = [(1,0),(0,1),(-1,0),(0,-1)]
Q = []

for i in range(N):
    for j in range(M):
        if data[i][j] == '1':
            Q.append((i,j))

cnt = 0

while Q:
    tmp = []
    for P in Q:
        for index in D:
            this=(P[0] + index[0],P[1] +index[1])
            if 0<= this[0] < N and 0 <= this[1] < M:
                if data[this[0]][this[1]] =='0' :
                    data[this[0]][this[1]] = '1'
                    tmp.append(this)
    Q = tmp[:]
    
    if Q:
        cnt +=1
    else:
        break
flag = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == '0':
            flag = 1
            break
if flag == 1: # 시행을 완료했음으도 불구하고 '0'인 지점이 발견되는 경우
    print(-1)
else:
    print(cnt)

'''아주 느림.
40650497	seob10278	7576	맞았습니다!!	148924	2908	Python 3 / 수정	874	2분 전
40650221	seob10278	7576	틀렸습니다			Python 3 / 수정	885	7분 전
40649974	seob10278	7576	틀렸습니다			Python 3 / 수정	856	11분 전
'''


# 다른 사람들은 어떻게 짰을까 ?
# 내가 마지막에 data전체에 대하여 '0'인 지점을 찾은 반면, 이 사람은 0인 포인트를 미리 세어두고 1로 바꾸면서 하나씩 줄여나갔음.
# deque 

import sys
from collections import deque
input = sys.stdin.readline


def solve():
    m, n = map(int, input().split())
    tomato = []
    haveto = 0
    tmt = deque()
    for i in range(n):
        tomato.append(input().split())
        for j in range(m):
            if tomato[i][j] == '0':
                haveto += 1
            elif tomato[i][j] == '1':
                tmt.append((i, j))
    res = 0
    while tmt and haveto:
        l = len(tmt)
        for _ in range(l):
            x, y = tmt.popleft()
            if x > 0 and tomato[x-1][y] == '0':
                tomato[x-1][y] = 1
                tmt.append((x-1, y))
                haveto -= 1
            if y > 0 and tomato[x][y-1] == '0':
                tomato[x][y-1] = 1
                tmt.append((x, y-1))
                haveto -= 1
            if x < n-1 and tomato[x+1][y] == '0':
                tomato[x+1][y] = 1
                tmt.append((x+1, y))
                haveto -= 1
            if y < m-1 and tomato[x][y+1] == '0':
                tomato[x][y+1] = 1
                tmt.append((x, y+1))
                haveto -= 1
        res += 1
    if haveto:
        print(-1)
    else:
        print(res)


if __name__ == '__main__':
    solve()

