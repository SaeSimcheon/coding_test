import sys
from collections import deque
sys.stdin = open('input.txt','r')

M,N,H = map(int,sys.stdin.readline().split())



data = [[sys.stdin.readline().split() for _ in range(N)] for __ in range(H)]

Q = deque([])
zero =0 
for h in range(H):
    for i in range(N):
        for j in range(M):
            if data[h][i][j] == '1':
                Q.append((h,i,j))
            elif data[h][i][j] == '0':
                zero +=1


D = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]

count =0
while Q :
    tmp = deque([])
    for P in Q:
        for index in D:
            #print(P)
            #print(index)
            this = (P[0]+index[0],P[1]+index[1],P[2]+index[2])
            if 0<=this[0] < H and 0 <= this[1] < N and 0 <= this[2] < M :
                if data[this[0]][this[1]][this[2]] == '0':
                    data[this[0]][this[1]][this[2]] ='1'
                    zero -=1
                    tmp.append(this)
    if tmp :
        count +=1
        Q = tmp
    else:
        break
if zero > 0 :
    print(-1)
else:
    print(count)


'''
40653996	seob10278	7569	맞았습니다!!	86960	4804	Python 3 / 수정	1069	17분 전
'''
