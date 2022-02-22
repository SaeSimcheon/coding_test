# 현재 입력과 일치하는 가장 긴 문자열을 찾음 -> 사전을 반대로 하는 것이 좋을 것 같음.
# 정규표현식 굳이 쓰지 않고 사전의 문자열 길이만큼 잘라내서 비교하는 것이 좋을 것 같음.
# 기억이 나지 않는 부분은 반드시 확인하고 넘어가기
# 부분부분 확인하면서 구현하기

def solution(msg):
    dictionary = {i+1:chr(65+i) for i in range(25,-1,-1)}
    print(dictionary)
    dict_end = 26 # 이 값에서 1까지 문자열이 매칭되는지 확인하고, 사전이 수정되면 1씩 키워줄 것임.
    n =5 # 임시로 확인해봄
    check =0 # check가 완료된 하위 문자열의 길이 -> 사용하지 않았음.
    answer = []
    print("a"[3:] == '')# 문자열의 index를 초과하여 slicing을 하는 경우 ''(아무 문자 없음)을 출력한다.
    # 이 사실을 이용하여 다음문자 여부를 파악하자.
    s = msg
    while s : # 문자열이 완벽하게 비어버리면 종료함.
        for i in range(dict_end,0,-1):
            candidate = dictionary[i]
            if s[:len(candidate)] == candidate : # 이게 같으면 색인 번호를 출력하고
                # s 길이가 0과 같은 경우는 전체 반복문 이탈
                answer.append(i)
                s = s[len(candidate):]
                #print(msg,candidate,answer)
                
                if s == '':
                # 이 부분이 가장 중요했는데 파이썬에서 문자열 slicing을 할때 존재하지 않는 index를 검색하는 것은 안 되지만, index 밖에서 :을 이용하여 slicing을 하는 경우에는 ''를 
                # 반환한다.
                    break
                else:
                #사전 수정하면 dict_end +=1
                # s가 ''가 아니면 반드시 적어도 문자 하나는 가지고 있으므로 아래 구문이 동작할 수 있다.
                    dict_end+=1
                    dictionary[dict_end] = candidate + s[0]
                    break
    
    return answer


# 현재 입력과 일치하는 가장 긴 문자열을 찾음 -> 사전을 반대로 하는 것이 좋을 것 같음.
# 정규표현식 굳이 쓰지 않고 사전의 문자열 길이만큼 잘라내서 비교하는 것이 좋을 것 같음.
# 기억이 나지 않는 부분은 반드시 확인하고 넘어가기
# 부분부분 확인하면서 구현하기

def solution(msg):
    dictionary = {i+1:chr(65+i) for i in range(25,-1,-1)}
    dict_end = 26 
    answer = []
    s = msg
    
    while s : 
        for i in range(dict_end,0,-1):
            candidate = dictionary[i]
            if s[:len(candidate)] == candidate : 
                answer.append(i)
                s = s[len(candidate):]
                if s == '':
                    break
                else:
                    dict_end+=1
                    dictionary[dict_end] = candidate + s[0]
                    break
    
    return answer



# 다른 사람들은 어떻게 풀었을까 ?


def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)} # 여기는 동일
    num = 27
    while msg: # msg를 직접 수정
        tt = 1 
        while msg[:tt] in tmp.keys() and tt <= msg.__len__(): # 길이가 tt
            tt += 1 # 만약 이탈을 못하면 tt를 증가시켜줌 나는 이거 반대로 하고싶었고, in 조건 쓰고 싶지 않았음.
            
        tt -= 1
        if msg[:tt] in tmp.keys(): # 더이상 사전안에서 탐색이 안 되면 이탈.이거 문자열 수정화는 과정에서 아마 '' 나오게 되지 않나 ?
            # 실행해본 것이 아니라서 잘 모르겠음
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num 
            num += 1 # 내 코드에서 dict_end 역할.
        msg = msg[tt:] # 나는 s라고 두고 풀었음.
    return answer
