# 답이 되었던 코드와 아주 결정적 차이는 if 0 <=nx <= 10**5 and not dist[nx]: 큐를 수정하는 데에서 옴
# 이미 방문한 것은 최소이므로 다시 큐에 넣지 않음. 방금 최초로 방문한 것은 큐에 넣음.
# 즉, 내가 짠 코드는 무분별하게 이미 최솟값을 갖게된 경우를 반복해서 방문하는 격임. 이미 최소이고 주변 값에 영향을 주었기 때문에
# 다시 방문할 이유 없음.
import sys
from collections import deque
sys.stdin = open('input.txt','r')

N , K = map(int,sys.stdin.readline().split())

def bfs(N_,K_):
    Q= deque([N])
    cnt =1
    end = 100000

    if N >= K :
        return N-K


    while True :
        tmp = deque([])
        flag=0
        
        for inq in Q:
            if 0<=inq-1 <=end :
                tmp.append(inq-1)
            if 0<=inq+1 <end:
                tmp.append(inq+1)
            if 0<=inq*2 <end:
                tmp.append(2*inq)
            if inq-1 == K or inq+1 == K or inq*2 == K:
                flag = 1
                break
        if flag == 0:
            Q = tmp
            cnt +=1 # 레벨을 세는 방식.
        else:
            break
    return cnt
print(bfs(N,K))




# bfs 진행하면서 최초로 등장하는 것은 최단 거리라는 뜻
# 이것이 중요한 사실
# 그런데 나는 왜 자꾸 시간 초과가 떴을까 ? -> 한 레벨 전체를 while 안의 한 반복에서 해결하려고 했기 때문 ?

import sys
from collections import deque
sys.stdin = open('input.txt','r')

N , K = map(int,sys.stdin.readline().split())



def bfs():
    q = deque()
    q.append(N)
    while q :
        x =q.popleft()
        if x ==K:
            print(dist[x])
            break
        for nx in (x-1,x+1,x*2):
            if 0 <=nx <= 10**5 and not dist[nx]:
                dist[nx] = dist[x] +1
                #print(dist[:K+2])
                q.append(nx)

dist = [0] * (10**5+1)
#print(dist[:K+2])
bfs()

'''dfs로 푼 방법도 있음.
def find(n, k):
    if n >= k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return min(find(n, k-1), find(n, k+1)) + 1
    else:
        return min(k-n, find(n, k//2) + 1)
  
import sys
n, k = map(int, sys.stdin.readline().split())
print(find(n, k))

'''

'''
end = 100000
DP = [0]*(max(N,K)+2)

for i in range(N-1,-1,-1):
    DP[i] = DP[i+1]+1
for jj in range(1,N+1):
    index = jj
    while True:
        #print(DP)
        index = index*2
        if N <index <len(DP):
            if DP[index]!=0:
                DP[index] = min(DP[index//2] +1,DP[index])
            elif DP[index]==0 :
                DP[index] = DP[index//2] +1
        if len(DP) <= index :
            break

for i in range(N+1,K+2):
    tmp = []
    
    if 0<=i-1<len(DP) :
        if DP[i-1]!=0 or i-1 == N:
            tmp.append(DP[i-1]+1)
    if 0<=i+1<len(DP) : 
        if DP[i+1] !=0 or i+1 == N: 
            tmp.append(DP[i+1]+1)
        
    if i %2 ==0 : tmp.append(DP[i//2]+1)
    if DP[i]!=0: tmp.append(DP[i])
    #print(DP,tmp)
    DP[i] = min(tmp) 


print(DP[K])
'''
# 나는 끝이 K 나 N 중 큰 쪽이면 될줄 알았는데
# 13 25 예시로 보면 내 지금 코드 기준 3이 나오는데 답은 2임
# 13에서 26으로 뛴 다음에 한 칸 뒤로가면 됨.
# 따라서 DP 길이는 1칸 더 길어야함.
# 그런데 그거보다 길어서 굉장히 적은 점에서 뛴 다음에 몇 칸 넘어오는 방법도 있지 않나 ?
# 그러면 최대 길이를 얼마로 설정해야할까 ?
