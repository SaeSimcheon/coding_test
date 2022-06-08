
- 포인트는 R 연산을 하지 않고 앞뒤에서 pop만 따로하는 것이었다고 생각.
- 전체 배열을 뒤집을때마다 시간이 오래 걸려서 시간 초과가 나왔다고 생각. 
- deque에 reverse는 콜랙션 전체를 뒤집어 줌.

```python
import sys
from collections import deque
sys.stdin = open('input.txt','r')

T = int(sys.stdin.readline())



def solution() :
    query = sys.stdin.readline().rstrip()
    
    N = int(sys.stdin.readline())
    
    A = sys.stdin.readline().rstrip()
    
    A = A.split(',')
    
    A[0]=A[0][1:]
    A[-1]=A[-1][:-1]

    if A[0] == '':
        A = deque()
    else:
        A = deque(A)

    direction = 1
    for i in query:
        
        if i == 'R':
            direction *=-1
        else:
            if len(A) == 0 :
                sys.stdout.write('error\n')
                return
            if direction == 1:
                A.popleft()
            else:
                A.pop()
    if direction == 1 :
        sys.stdout.write(f"[{','.join(A)}]\n")
    else:
        A.reverse()
        sys.stdout.write(f"[{','.join(A)}]\n")
    
    return

for _ in range(T):
    solution()
```

## 다른 사람들은 어떻게 풀었을까 ?
- RR을 '

```python
from sys import stdin

input = stdin.readline


def solve():

    for _ in range(int(input())):
        # 'RR' 는 안뒤집는 것과 동일하므로 ''로 바꿔준다
        p = [*map(len, input()[:-1].replace('RR', '').split('R'))]

        n = int(input())
        arr = input()[1:-2].split(',')
        # [left, right) 가 출력된다
        left, right = sum(p[::2]), n - sum(p[1::2])

        if left <= right:
            # len(p) % 2 == 1 인 경우 왼쪽에서 오른쪽 방향
            arr = arr[left:right] if len(p) % 2 else reversed(arr[left:right])
            print(f"[{','.join(arr)}]")
        else:
            print('error')


if __name__ == '__main__':
    solve()

```
