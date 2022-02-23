# 내가 진수 구하는 방식이 뭔가 이상한가?
def transform(num,k):
    sub = ["A","B","C","D","E","F"]
    if num < k :
        if num >=10: 
            num = sub[num-10]
        return str(num)
    remain = ''
    sol = ''
    # while num>=k:  이거 판단하는데에 아래에서 A B C D E F 로 바꿔서 error가 남.
    while True : 
        num,remain = divmod(num,k)
        
        if remain >=10:
            remain = sub[remain-10]
        sol = str(remain) + sol
        if num < k:
            if num >=10:
                num = sub[num-10]
            sol = str(num) + sol
            break
        
    
    return sol

def solution(n, t, m, p):
    # n 진법
    # t 미리 구할 숫자 개수
    # m 참여 인원
    # 튜브의 순서 p 튜브가 말할 순서의 문자를 개수만큼 출력해야함.
    
    # 예시로 몇 개 구해보자
    
    # t 번만큼 대답할 것
    # m 명이 참여
    # tm만큼 미리 구해서 ->
    # p번 주기 만큼 확인하자
    need = m*t # d 참여인원이 t만큼 말할 수 있을 문자열까지 만들자
    
    
    string = ''
    
    # 아래 반복문에서 런타임 에러 발생함.
    # 문자열이 너무 길 수도 있나 ?
    # m*t는 최대 얼마지 ?
    # 100 * 1000 = 10만 -> 10만의 문자열 좀 많은 것 같기도 하고
    # 문자열을 저장해서 쓸 수 없으면 어떡하지 ? -> 한 번 생성한 문자열 안에서 해결해야하나 ?
    obj=0
    while need > len(string): 
        add = transform(obj,n) 
        string += add
        obj+=1
        
        
    answer = ''    
    # 주가는 m임
    # p-1로 indexing 시도하는데 p==1인 경우가 자꾸 문제가 됨
    # index%p-1 == 0로 시도 하면 0으로 나누는 꼴이됨
    
    turn =0 
    
    
    while len(answer) < t:
        answer += string[p +m*turn-1]
        turn +=1
        
    return answer



# 21:28 틀린 것은 없는데 런타임 에러 발생함. -> 해결
def transform(num,k):
    sub = ["A","B","C","D","E","F"]
    if num < k :
        if num >=10: 
            num = sub[num-10]
        return str(num)
    remain = ''
    sol = ''
    
    while True : 
        num,remain = divmod(num,k)
        
        if remain >=10:
            remain = sub[remain-10]
        sol = str(remain) + sol
        if num < k:
            if num >=10:
                num = sub[num-10]
            sol = str(num) + sol
            break
    return sol

def solution(n, t, m, p):
    need = m*t 
    string = ''
    obj=0
    
    while need > len(string): 
        add = transform(obj,n) 
        string += add
        obj+=1
    answer = ''    
    turn =0 
    
    while len(answer) < t:
        answer += string[p +m*turn-1]
        turn +=1
        
    return answer





