## 0529
- https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#Solution_for_two_sequences
```python
import sys

sys.stdin = open('input.txt','r')

S = sys.stdin.readline().rstrip()
D = sys.stdin.readline().rstrip()



DP = [[0 for _ in range(len(D)+1)] for _ in range(len(S)+1)]


answer =0

S = ' '+S
D = ' '+D

for i in range(1,len(S)):
    for j in range(1,len(D)):

        if S[i] == D[j]:
            DP[i][j] =  DP[i-1][j-1]+1
        else:
            DP[i][j] =  max(DP[i][j-1],DP[i-1][j])
    if answer < DP[i][j]:
        answer = DP[i][j]

print(answer)



    

            
                
                
```
