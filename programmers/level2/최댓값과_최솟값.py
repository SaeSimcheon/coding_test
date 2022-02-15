# 첫번째 시도 (통과)
# 문자열 안에서 최대 최소를 찾아서 -> '(최소) (최대)' 형태로 return하는 문제.
# split map +을 통한 문자열 합치기
def solution(s):
    
        
    s=s.split(' ') # 일단 공백 기준으로 문자열을 구분자로해서 리스트로 만들겠다고 생각.
    # int로 만들어야 예상되는 답안대로 대소 구분이 될 것이라고 생각.
    s=list(map(lambda x: int(x),s))
    # 이 방법 말고도 split과 int를 한 함수에 처리하게 해서 map을 적용하는 방법도 있다고 생각.
    # map이 기억이 안 나서 떠올리는 데에 시간이 걸림.
    
    

    
    
    return str(min(s))+' '+str(max(s))

# map 함수에 대해서 정리하자
# 구분자라는 표현이 어색하므로 정리하자
# list comprehension에서 만약 조건에 안 맞으면 그냥 원소 자체를 list에 포함하지 않는 방법도 있을까 ?


# 다른 사람들은 어떻게 풀었을까 ?

# 


def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
