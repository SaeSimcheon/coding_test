# 첫번째 시도 
# python에는 정수를 이진수로 만드는 함수 bin이 있어서 그대로 이용하면 된다고 생각했음.
# 만약 bin이 없다면 직접 이진수를 만드는 함수를 사용해야함.
# 1번 조건의 경우 후보를 n +1부터 시작함으로써 간단하게 해결했음.


def solution(n):
    answer = 0
    # 조건 2 이진수 변환 조건
    # 1 2 만족하는 더 작은 수
    # bin 함수 이용하면 될 것 같은데
    # 해서 string으로 만든 다음 1 count
    num_one = str(bin(n))
    num_one=num_one.count('1')
    answer = n+1
    while True :
        a=str(bin(answer))
        a=a.count('1')
        if a == num_one:
            break
        answer+=1
     
    return answer
