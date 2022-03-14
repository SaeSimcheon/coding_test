# 느림. 불필요한 
import sys
sys.stdin = open('input.txt','r')
N,M,V=map(int,sys.stdin.readline().split())
mat=[[0]*N for _ in range(N)]
mat_bfs=[[0]*N for _ in range(N)]

for i in range(M):
    start,end=map(int,sys.stdin.readline().split())
    mat[start-1][end-1] = 1
    mat[end-1][start-1] = 1
    mat_bfs[start-1][end-1] = 1
    mat_bfs[end-1][start-1] = 1

dfs_str = f'{V}'
ch_dfs = [0]*N
ch_dfs[V-1]=1
def dfs(index):
    global dfs_str
    if sum(mat[index]) == 0 :
        return
    for ind,i in enumerate(mat[index]):
        
        if i == 1 and ch_dfs[ind] ==0:
            dfs_str +=' ' + str(ind+1)
            mat[index][ind] =0 
            mat[ind][index] =0 
            ch_dfs[ind] = 1
            dfs(ind)

dfs(V-1)
print(dfs_str)

# bfs
queue=[V-1]
ch = [0]*N
ch[V-1] =1
bfs_str = f'{V}'
while queue:
    point=queue.pop(0)
    for index,i in enumerate(mat_bfs[point]):
        if i ==1 and ch[index] == 0:
            bfs_str += ' '+str(index+1)
            queue.append(index)
            ch[index] = 1
print(bfs_str)
