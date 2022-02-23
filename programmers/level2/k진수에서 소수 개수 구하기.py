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
    


# 결국 여러 사람들 질문들 참고해서 해결함
# prime 판별에서 메모리 문제가 있었음.
# check list를 만드는 데에 숫자가 너무 크면 메모리 문제를 발생.
# 결국 list를 만들지 않고 소수를 개별적으로 판별하는 방법을 선택했음.
# 처음에는 n//2+1을 끝값으로 해서 시간을 아껴보려 했지만, 성공하지 못함
# int(n**0.5) +1가 최선이라는 것을 발견하고 시도해본 결과 성공함.

# 다른 접근들은 틀리지 않았음.
    
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
    #ch =  [0]*(element//2+1)# 이 코드가 메모리를 크게 잡아먹는 듯
    # 가장 효율적인 소수 판별은 어떻게 하더라 ?
    # 체크 리스트를 쓰지 않고 에라토스테네스 체를 사용하는 방법
    # int(element**0.5)+1을 사용해도 소수 판별이 가능함
    for i in range(2,int(element**0.5)+1):
        if element % i ==0 :
            return False
    return True
    
    
def solution(n, k):
    #n,k=524287,2
    
    # 1번 11번에서 에러가 나는데 1번의 답은 1임
    # 보니까 prime 함수에서 에러가 남. 
    # transformed가 의도하지 않은 형태로 이루어진 경우도 에러가 일어날 가능성이 있기 때문에 
    # 두 함수 모두 확인해야함.
    # 19:43 다른 사람들도 푸는 것보니까 1번 틀린 사람들이 시도해본 테스크 케이스 주워서
    # 시도해 보니까 524287 , 2 메모리 에러 뜸
    # 프라임에서가 문제인듯
    transformed= transform(n,k)
    
    if transformed.count('0') == 0 :
        if prime(transformed) == True :
            return 1
        else:
            return 0
    transformed=transformed.split('0')# 중간에 0으로 연속인 경우에는 ''가 생김.
    
    check_prime = list(map(lambda x : prime(x),transformed))
    
    #print(check_prime)
    
    
    return sum(check_prime)
