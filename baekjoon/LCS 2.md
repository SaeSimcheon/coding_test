## 0604
- 

```python
import sys

sys.stdin =open('input.txt','r')

A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())

length_A = len(A)
length_B = len(B)


A = [""] + A
B = [""] + B



mat = [[0 for _ in range(length_B+1)] for _ in range(length_A+1)]

track = [['' for _ in range(length_B+1)] for _ in range(length_A+1)]


for i in range(1,length_A+1):
    for j in range(1,length_B+1):
        if A[i] == B[j] :
            mat[i][j] = mat[i-1][j-1] +1
            track[i][j] = track[i-1][j-1] +A[i]
        else:
            if mat[i][j-1] > mat[i-1][j]:
                mat[i][j] = mat[i][j-1]
                track[i][j] = track[i][j-1]
            else:
                mat[i][j] = mat[i-1][j]
                track[i][j] = track[i-1][j]
print(mat[-1][-1])
print(track[-1][-1])

```
