[참고1](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)
[참고2](https://sites.radford.edu/~nokie/classes/360/dp-knapsack.html)

- i 번째 아이템까지 사용했을때 weight j에서의 최대.
- 만약 현재 weight을 넘는 경우에는 이전 아이템까지의 최대를 사용. 
  - mat[i][j] = mat[i][j-1]

- 모든 weight의 상태에서 i 번째 아이템의 weight 반영.


- 만약 i 번째 아이템을 넣을 수 있는 경우 두 가지 경우를 따짐. 두 경우 중에서 더 큰 경우를 선택함.
  - 아이템을 넣음. -> mat[i][j-A[i][0]]+A[i][1]
  - 아이템을 넣지 않음. -> mat[i][j-1]
  
- 모든 0부터 w까지 따짐.





```python
seq = [[0,0]] + [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
mat = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(N+1):
    for j in range(K+1):
        if i == 0 or j == 0 :
            mat[i][j] = mat[i-1][j]
        else:
            if seq[i][0] > j :
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = max(mat[i-1][j],mat[i-1][j-seq[i][0]] +seq[i][1])
```

- 2d array approach

![image](https://user-images.githubusercontent.com/49121293/171551751-636561c4-b79d-4dfb-9bfa-446ad359c587.png)



- 1d array approach
뒤부터 순회

```python
for i in range(N):
    for j in range(K,-1,-1):
    #for j in range(0,K+1):            
        if j >= seq[i][0]:
            mat[j] = max(mat[j],mat[j-seq[i][0]] +seq[i][1])
        if answer < mat[j]:
            answer = mat[j]
        print(mat)
'''

[0, 0, 0, 0, 0, 0, 0, 13]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 0, 0, 13, 13]
[0, 0, 0, 0, 0, 8, 13, 13]
[0, 0, 0, 0, 8, 8, 13, 13]
[0, 0, 0, 0, 8, 8, 13, 13]
[0, 0, 0, 0, 8, 8, 13, 13]
[0, 0, 0, 0, 8, 8, 13, 13]
[0, 0, 0, 0, 8, 8, 13, 13]
[0, 0, 0, 0, 8, 8, 13, 14]
[0, 0, 0, 0, 8, 8, 13, 14]
[0, 0, 0, 0, 8, 8, 13, 14]
[0, 0, 0, 0, 8, 8, 13, 14]
[0, 0, 0, 6, 8, 8, 13, 14]
[0, 0, 0, 6, 8, 8, 13, 14]
[0, 0, 0, 6, 8, 8, 13, 14]
[0, 0, 0, 6, 8, 8, 13, 14]
[0, 0, 0, 6, 8, 8, 13, 14]
[0, 0, 0, 6, 8, 8, 13, 14]
[0, 0, 0, 6, 8, 12, 13, 14]
[0, 0, 0, 6, 8, 12, 13, 14]
[0, 0, 0, 6, 8, 12, 13, 14]
[0, 0, 0, 6, 8, 12, 13, 14]
[0, 0, 0, 6, 8, 12, 13, 14]
[0, 0, 0, 6, 8, 12, 13, 14]
'''
```
