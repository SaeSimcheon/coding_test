# stack이 먼저 떠오름.
# stack에 여는 괄호를 넣는다고 가정하면
# stack이 차있는 상태로 종료되거나
# stack에 뺄 것이 없는데 닫는 경우

def solution(s):
    stack = []
    s = list(s[::-1]) # pop 하기 위해서 문자열을 한 번 뒤집음
    answer = True # true로 시작함.
    while s :
        one=s.pop()
        if one == '(':
            stack.append(one)
            continue
        else:
            if len(stack)== 0: # stack ')'가 문자열에서 pop 되었는데, stack이 비어있으면 쌍이 안 맞는 것임.
                answer = False
                break
            else:
                stack.pop()
                continue
    if len(stack) !=0: # s에서 더 이상 pop 할 것이 없음에도 불구하고 stack의 길이가 1보다 크다면 쌍이 안 맞는 것.
        answer = False
    
    return answer
