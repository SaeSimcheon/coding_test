## 0527
- 프로그래머스 문제중에도 똑같은 방식으로 해결할 수 있는 문제가 있음.
- 하향식으로 해결했는데 sequence 크기가 고정되어 있고, i 번째 행이 R,G,B를 각각 색칠 했을 때의 최소 비용인 메모이제이션 정의할 수 있었음.

```python
import sys

sys.stdin = open('input.txt','r')

N=int(sys.stdin.readline())



seqs =[]

for _ in range(N):
    seq =list(map(int,sys.stdin.readline().split()))
    seqs.append(seq)

for i in range(1,N):
    seqs[i][0] += min(seqs[i-1][1],seqs[i-1][2])
    seqs[i][1] += min(seqs[i-1][0],seqs[i-1][2])
    seqs[i][2] += min(seqs[i-1][0],seqs[i-1][1])


print(min(seqs[-1]))

```
