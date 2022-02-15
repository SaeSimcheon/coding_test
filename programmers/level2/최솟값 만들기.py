# 첫번째 풀이

# 시간 초과 나옴.

# A와 B 원소 각각을 곱해 더했을때 최소가 되는 경우의 값 구하기.
# 이거 dfs ?
# 반복문으로 A를 쭉 탐색하는데 checklist를 만들어서 B에 대한 경우의 수를 따지는 방법
def solution(A,B):
    answer = 20000000000# python에서 최댓값 설정 어떻게 하더라 ? float('inf')아니었나 ?
    ch = [0]*len(B)
    
    def dfs(index , candidate):
        nonlocal answer
        if (index != len(B))&(answer < candidate):
            return
        if index == len(B):
            if answer > candidate :
                answer = candidate
            return
        else:
            for i in range(len(B)):
                if ch[i] == 1:
                    continue
                else:
                    ch[i] = 1
                    dfs(index+1,candidate +A[index]*B[i] )
                    ch[i] = 0
    
    dfs(0,0)
    

    return answer
    
# 옛날에 풀었던 것인데 기억이 안남



# 두번째 풀이 ()
# A는 그냥 순회하고 B는 그때그때 그냥 큰를 곱하면 된다?
def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
   
    for i in range(len(B)):
        answer+= A.pop(0) * B.pop()
        
    
    
    

    return answer


# sort의 reverse =True 옵션을 통해서 아래 반복문에서 pop()를 사용하게 함. 
# pop(0)가 시간 복잡도로 O(n)을 갖는다고 들었기 때문에


def solution(A,B):
    answer = 0
    
    A.sort(reverse = True)
    B.sort()
    
    for i in range(len(B)):
        answer+= A.pop() * B.pop()
        
    
    
    

    return answer


## 그나저나 왜 저게 답이 될까?
## 그때그때 최솟값을 갖도록 하는 조합을 선택하는 문제로 greedy algorithm과 상관 있어 보인다.

## https://programmers.co.kr/questions/15949
## 이거 참고하면 greedy selection property로 증명해야



## D+1 

# 그때그때 최소가 되는 조합으로 따지면 결과적으로 최솟값을 만들 수 있음.
# A를 내림차순으로 정렬 후에 고정으로 두고 B에서 수를 골라 조합을 맞춘다고 가정했을때, 
# A가 작아짐에 따라서 B를 작은 순서에서 큰 순서로 선택하면 답이 됨. -> B는 오름차순으로 정렬

# A와 B의 개수가 같고 앞에서 정렬한다고 가정했으므로 zip을 이용한 반복문을 사용할 수 있을 것이라는 생각을 할 수 있음.


def solution(A,B):
    answer = 0
    
   있
    A.sort(reverse = True)
    B.sort()
    
    for i , j in zip(A,B):
        answer += i*j

    return answer
