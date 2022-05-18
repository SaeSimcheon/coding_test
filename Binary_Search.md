
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
