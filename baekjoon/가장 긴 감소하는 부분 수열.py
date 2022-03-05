# 풀긴 풀었는데 해가 정확히 마지막에 완벽하게 F[N-1]로 설계를 안 해서 잘 푼건지 확신이 안 섬
# 

import sys
sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline())

data = list(map(int,sys.stdin.readline().split()))


def solution():
    F = [1]

    for i in range(1,N):
        flag = 0
        #print(F)
        candidate = 0
        for j in range(i-1,-1,-1):
            if data[i] < data[j] and candidate < F[j]+1:
                candidate = F[j]+1
                flag = 1
        if flag ==0:
            F.append(F[j])
            continue
        F.append(candidate)
    print(max(F))


    
solution()




# 다른 사람들 풀이1

def sol(N, seq):
    result = [seq[0]]
    index = 0
    for i in range(1, N):
        if result[index] > seq[i]:
            result.append(seq[i])
            index += 1
        else:
            for j in range(index + 1):
                if result[j] <= seq[i]:
                    result[j] = seq[i]
                    break
    index += 1
    return index
  


if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    print(sol(N, seq))

# 다른 사람들 풀이2    

def lower_bound(s, e, t):
    while s < e:
        m = (s + e) // 2
        if lds[m] > t:
            s = m + 1
        else:
            e = m
    return e

  
N = int(input())
arr = list(map(int, input().split()))
lds = []
for i in range(N):
    if i == 0:
        lds.append(arr[i])
        continue
    if lds[-1] > arr[i]:
        lds.append(arr[i])
    else:
        tmp = lower_bound(0, len(lds), arr[i])
        lds[tmp] = arr[i]
print(len(lds))


# 다른 사람들 풀이3
def lis_reverse(arr):
    def binary_search(arr, val, lo, hi):
        while lo < hi:
            mid = (lo+hi) // 2
            if val >= arr[mid]:
                hi = mid
            else:
                lo = mid + 1

        return lo

    ordered = []

    for val in arr:
        searched_idx = binary_search(ordered, val, 0, len(ordered))
        if searched_idx >= len(ordered):
            ordered.append(val)
        else:
            ordered[searched_idx] = val

    return len(ordered)

num = int(input())
arr = list(map(int, input().split()))
print(lis_reverse(arr))
