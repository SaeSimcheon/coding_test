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
    ch = [0]*len(B)
    
    A.sort()
    B.sort()
   큰
    for i in range(len(B)):
        answer+= A.pop(0) * B.pop()
        
    
    
    

    return answer
