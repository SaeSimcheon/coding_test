# 1로 이동 -> 점프 
# 현재까지 온 거리 x 2인 위치로 이동 가능.
# 1 인 경우 1
# 2인 경우 1
# 3인 경우 2
# 4인 경우 2
# 5인 경우 2
# 6인 경우 2
# 7인 경우 
# 8인 경우 2
# 9인 경우 
# 10인 경우 2
# 2의 배수면 1/2의 수에서 사용한 수만큼 이용하면 됨.
# 5000 2500 1250 625 
# -1 한 다음에 2로 계속 나눈 다음 -1 하는 것 아닐까 ?
# 5000 2500 1250 625-624 312 156 78 39-38 19-18 9-8 4 2 1-
def solution(n):
    ans = 1
    # 결론은 홀짝 규칙이었음.
    
    while n !=1 :
        if n %2 ==0:
            n //=2
            continue
        else:
            n-=1
            ans+=1
    
    
    return ans


# 다른 사람 풀이
# ㅋㅋㅋ
def solution(n):
    return bin(n).count('1')
