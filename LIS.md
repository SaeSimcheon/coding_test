## LIS with binary searching

```python
import sys

sys.stdin = open('input.txt','r')
N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))

P = [0]*N
M = [0]*(N+1)

M[0] =-1

L =0

for i in range(N):
    lo = 1
    hi = L +1

    while lo < hi :
        mid = (lo+hi)//2
        if A[M[mid]] < A[i]:
            lo = mid +1
        else:
            hi = mid

    newL = lo
    print(A[i],newL) # newL 바뀔 수 있음.
    # M 안에서 탐색 일어남.
    # 값이 같으면 좌측에서 더 탐색

    P[i] = M[newL-1] # X[k]를 마지막으로 갖는 가장 긴 수열에서 
    # X[k] 이전의 인덱스
    M[newL] = i

    if newL > L:
        L = newL
    print("P",P)
    print("M",M)
    
S = [0]*L
k = M[L]

for j in range(L-1,-1,-1):
    S[j] = A[k]
    print(k)
    k = P[k]
print(len(S))
```
