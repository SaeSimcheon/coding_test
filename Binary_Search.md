
- 방식에 약간씩 차이들이 있음.
[wiki](https://en.wikipedia.org/wiki/Binary_search_algorithm#Duplicate_elements)

## Lower bound

- 목표하는 값보다 **크거나 같은 값** 중 가장 왼쪽 위치.
- 15557에서 5를 타겟을 잡으면 1(X)5557를 가리킴.
```python
if data[med] >= given : # 크거나 값이 같은 경우
  b = point -1          # 가장 왼쪽 위치 탐색
else:
  a = point +1
```

- 위키피디아에 있는 수도 코드

```
function binary_search_leftmost(A, n, T):
    L := 0
    R := n
    while L < R:
        m := floor((L + R) / 2)
        if A[m] < T:
            L := m + 1
        else:
            R := m
    return L
```

## Upper bound

- 목표하는 값보다 **큰 값** 중 가장 왼쪽 위치.
- 15557에서 5를 타겟을 잡으면 1555(X)7를 가리킴.
```python
if data[med] >= given : # 값이 큰 경우
  b = point -1          # 가장 왼쪽 위치 탐색

else :
  a = point +1
```

```
function binary_search_rightmost(A, n, T):
    L := 0
    R := n
    while L < R:
        m := floor((L + R) / 2)
        if A[m] > T:
            R := m
        else:
            L := m + 1
    return R - 1

```


```python


A = [10, 10, 20, 20, 20, 30, 50]
def lower_bound(given):
    a = 0
    b = len(A)-1
    print('start',a,b)
    while a <=b :

        point = (a+b) //2

        if A[point] >= given :
            b = point -1
        else:
            a = point +1
        print("a,b,point,case")
        print(a,b,point,A)
    
    return a 

def upper_bound(given):
    a = 0
    b = len(A)-1
    print('start',a,b)
    while a <=b :

        point = (a+b) //2

        if A[point] > given :
            b = point -1
        else:
            a = point +1
        print("a,b,point,case")
        print(a,b,point,A)
    
    return a 


print(lower_bound(20))
print(upper_bound(20))

```
```
[10, 10, 20, 20, 20, 30, 50]
start 0 6
a,b,point,case
0 2 3 [10, 10, 20, 20, 20, 30, 50]
a,b,point,case
2 2 1 [10, 10, 20, 20, 20, 30, 50]
a,b,point,case
2 1 2 [10, 10, 20, 20, 20, 30, 50]
2
start 0 6
a,b,point,case
4 6 3 [10, 10, 20, 20, 20, 30, 50]
a,b,point,case
4 4 5 [10, 10, 20, 20, 20, 30, 50]
a,b,point,case
5 4 4 [10, 10, 20, 20, 20, 30, 50]
5

```


### Rightmost case
- return 에서 b 로 설정하면 upper bound
```python
def upper_bound(given):
    a = 0
    b = len(A)
    print('start',a,b)
    while a <b :
        point = (a+b) //2
        if A[point] > given :
            b = point
        else:
            a = point +1
        print("a,b,point,case")
        print(a,b,point,A)
    
    return b-1
```
### Leftmost 

- lower bound
- 이 형태로 아는 것이 좋을듯

```python
def lower_bound(given):
    a = 0
    b = len(A)
    print('start',a,b)
    while a <b :

        point = (a+b) //2

        if A[point] >= given :
            b = point
        else:
            a = point +1
        print("a,b,point,case")
        print(a,b,point,A)
    
    return a 

```

```0525

import sys

sys.stdin = open('input.txt','r')


A=list(map(int,sys.stdin.readline().split()))



L = 0
R = len(A)

T = 4
while L < R :
    mid = (L + R )//2

    if A[mid] < T :
        L = mid+1
    elif A[mid] >T :
        R = mid
    elif A[mid] == T:
        R = mid
print(A)
print(L)


L=0
R=len(A)

while L < R :
    mid = (L+R) //2

    if A[mid] < T :
        L = mid +1
    elif A[mid] > T :
        R = mid
    elif A[mid] == T :
        L = mid +1
print(A)
print(R-1) # right most
print(R) # upper bound

'''
A = [1, 2, 3, 4, 4, 4, 5, 6, 7]
[1, 2, 3, 4, 4, 4, 5, 6, 7]
3
[1, 2, 3, 4, 4, 4, 5, 6, 7]
5

[1, 2, 3, 100, 101, 102]
3
[1, 2, 3, 100, 101, 102]
2
3

- target 값이 sequence 안에 없는 경우
L과 R이 가리키는 곳이 같음.
- 그 값이 위치해야하는 자리

1 2 3 5 6 7


'''

```


# left and right most에 대한 Wiki pseudocode 기준 구현 팁

## while 안의 if 문 '==일때 차이에 집중.'

### left most는 기준 값과 같을때 왼쪽으로 당겨옴.

```python

if A[m] < T :
  L = m +1
elif A[m] > T :
  R = m
elif A[m] == T :
  R = m
```

### right most는 기준 값과 같을때 오른쪽으로 당겨옴.

```python
if A[m] < T :
  L = m+1
elif A[m] >T :
  R = m
elif A[m] == T :
  L = m+1
```

- return은 각각 L과 R-1

## 기준 값이 없는 경우에 L과 R이 가리키는 위치가 같음.

- 어떤 수가 있어야하는 위치를 가리킴


```
T = 4
[1, 2, 3, 100, 101, 102]
L = 3
[1, 2, 3, 100, 101, 102]
R -1 = 2
R = 3

```


