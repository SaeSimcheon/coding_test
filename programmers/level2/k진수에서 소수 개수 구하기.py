# k 진수를 계산하는 함수
# divmod -> 몫과 나머지를 반환하는 함수
# 진법으로 나타내는 함수 공부해보기

def transform(n,k):    
    remain = ''
    sol = ""
    if n < k :
        return str(n)
    while n >=k:
        n,remain=divmod(n,k)
        sol = str(remain) + sol
        if n < k :
            sol = str(n) + sol
    return sol

# 0이 일종의 구분자 처럼 쓰임.
# 0을 그냥 구분자로 두면 안 되나 ?
# 0P0 -> 0 사이에 끼어있음. 
# P0 -> 문자열 왼쪽 끝
# 0P 문자열 오른쪽 끝
# P -> 그 자체로 소수임 -> 가장먼저 조사해야할 것. 단, P는 0을 포함하지 않음. -> 0이 있는지 검색 ? -> 0을 포함하는 소수는 있을 수 있지 않나 ? 아 p는 아예 포함하지 않네
# 그럼 0이 구분자가 될 수 있음
# 101은 p가 될 수 없음.

# 1번 자꾸 런타임 에러가 발생하길래 

def prime(element):
    if element == '' or element == '1':
        return False
    element = int(element)
    ch =  [0]*(element+1)
    
    for i in range(2,element+1):
        if ch[i] == 0:
            for j in range(i*2,element+1,i):
                ch[j] = 1
    
    return ch[element]  ==0
    
def solution(n, k):
    # 1번 11번에서 에러가 나는데 1번의 답은 1임
    # 보니까 prime 함수에서 에러가 남. 
    # transformed가 의도하지 않은 형태로 이루어진 경우도 에러가 일어날 가능성이 있기 때문에 
    # 두 함수 모두 확인해야함.
    
    transformed= transform(n,k)
    
    if transformed.count('0') == 0 :
        if prime(transformed) == True :
            return 1
        else:
            return 0
    transformed=transformed.split('0')# 중간에 0으로 연속인 경우에는 ''가 생김.
    
    check_prime = list(map(lambda x : prime(x),transformed))
    
    #print(check_prime)''
    
    
    return sum(check_prime)
    
