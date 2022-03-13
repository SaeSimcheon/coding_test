# 
import sys

sys.stdin = open('input.txt','r')
str1=str(sys.stdin.readline()).rstrip()
str2=str(sys.stdin.readline()).rstrip()

print(str1)
print(str2)

N = len(str1)
DP = [[[''] for _ in range(N)] for __ in range(N)]




def make_candidate(arr1,arr2):
    # arr1 -> DP[j][k]
    # arr2 -> DP[k+1][i]
    candidate = []
    max_len = 0
    for i in arr1:
        for j in arr2:
            string = i + j
            comp = list(set(string))
            comp.sort()
            comp=''.join(comp)
            if comp == string :
                if len(string) > max_len:
                    max_len = len(string)
                candidate.append(string)
    if len(candidate ) == 0: candidate.append('')
    print(candidate)
    return candidate , max_len


for ii in range(0,N):
    can = list()
    for index,ch in enumerate(str2):
        #print(ch)
        if str1[ii] == ch : can.append(str(index))
    DP[ii][ii] = can

print(DP)

for i in range(0,N) :
    for j in range(i, -1 , -1):
        finding = list()
        
        if i == j :continue
        max_len =0
        for k in range(j,i):
            
            result,length=make_candidate(DP[j][k], DP[k+1][i])
            if length >max_len :
                max_len=length
            
            finding+=result
            
            print(j,i,k,finding)
            print(DP[j][k],DP[k+1][i])
        DP[j][i]= [kk  for kk in finding if  len(kk)==max_len]            
        
print(DP)
