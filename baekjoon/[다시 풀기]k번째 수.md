## https://kbw1101.tistory.com/29
- 
```python

import sys

sys.stdin = open('input.txt','r')
N = int(sys.stdin.readline())
k = int(sys.stdin.readline())



a = 1

b = k

answer =0
while a <= b :
    point = (a+b)//2
    cnt=0
    for i in range(1,N+1):
        cnt += min(N,point//i)
    
    if cnt >=k :
        answer = point
        b = point -1
    else :
        a = point +1
print(answer)
```
