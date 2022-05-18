


## Lower bound

- 목표하는 값보다 **크거나 같은 값** 중 가장 왼쪽 위치.

```python
if data[med] >= given : # 크거나 값이 같은 경우
  b = point -1          # 가장 왼쪽 위치 탐색
else:
  a = point +1
```

## Upper bound

- 목표하는 값보다 **큰 값** 중 가장 왼쪽 위치.

```python
if data[med] >= given : # 값이 큰 경우
  b = point -1          # 가장 왼쪽 위치 탐색

else :
  a = point +1
