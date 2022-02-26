# dfs에서 그냥 return 하는 것과 값이 있는 것
# dfs 함수 순서 구조
# dfs 안에서 함수 밖의 자료 수정

def dfs(index,remain,score,vec,info):    
    global answer,answer_vec
    #print(index,remain,info,candidate)
    if remain < 0 :
        return 
    if index == 11 and remain !=0: return 
    if remain == 0 :
        peach = [ 10-index if i !=0 and j==0 else 0 for index,(i,j) in enumerate(zip(info,vec))]
        if answer == score -sum(peach):
            print(answer_vec)
            for i, j in zip(answer_vec[::-1],vec[::-1]):
                if i > j :
                    break
                if i < j :
                    answer_vec = vec[:]
        if answer < score-sum(peach):
            print(answer_vec)
            answer = score-sum(peach)
            answer_vec = vec[:]
        return 
        # remain이 0이지만 index가 10이 아닌 경우에는 나머지 점수 다 계산해야함.
        # 무슨 차이일까 global로 선언 해준 뒤에 [:] 이렇게 안 해주면
            # vec을 대입한 결과가 반영이 안 됨 -> 깊은 복사를 안 했다 ?
    #if index != 10:
    if index == 10 : # 개 억지로 품
        print(vec,remain)
        vec[index] += remain
        print(vec,remain)
        dfs(index+1,0,score + 10 - index,vec,info)
        vec[index] -= remain
        dfs(index+1,remain,score,vec,info)
        
    vec[index] += info[index]+1
    dfs(index+1,remain-(info[index]+1),score + 10 - index,vec,info)
    vec[index] -= info[index]+1
    dfs(index+1,remain,score,vec,info)
    '''
    else:
        vec[index] += remain
        dfs(index+1,remain-remain,score + 10 - index,vec,info)
        vec[index] -= remain
        dfs(index+1,remain,score,vec,info)
        '''
    
    


def solution(n, info):
    global answer,answer_vec
    answer_vec = []
    answer = 0
    candidate = [0]*len(info)
    #print(candidate)
    dfs(0,n,0,candidate,info)
    print(f"end : {answer_vec} , answer : {answer}")
    
    if len(answer_vec) == 0:
        return [-1]
    
    return answer_vec
