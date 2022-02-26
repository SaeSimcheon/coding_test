# 가장 큰 정사각형의 넓이는 작은변**2임.
# 한 포인트 기준으로 탐색
# 전체 순회하며 탐색
def filter(start,length,mat):
    
    flag = 0
    
    for i in range(start[0],start[0]+length):
        for j in range(start[1],start[1]+length):
    
            if mat[i][j] == 0 : # 만약 0인 부분이 나오면 flag를 1로 두고 break 함.
                # 넓이 조건이 만족이 안 되면 flag 1로 return 됨
          # 지점이 0인 것을 발견하면 다음 start point에서 제외하면 됨.
                flag = 1
                break
        if flag == 1:
            break
    return flag

def iteration(length,mat):
    
    flag = 0
    
    # 0 이 리턴되면 해당 start point에서 
    
    for i in range(0,len(mat)-length +1):
        for j in range(0,len(mat[0]) - length+1):
            check=filter([i,j],length,mat)
            if check == 0: # 
                flag = 1
                break
        if flag == 1 :
            break
    
    return flag
    



def solution(board):
    height = len(board)
    width = len(board[0])
    length=min(width,height)
    
    answer = length
    while answer > 1 :
        flag = iteration(answer,board)
        
        if flag == 1:
            break
        answer -=1 # 길이 1씩 줄여가는게 지나치게 오래걸리는게 아닐까 ?
    
    return answer **2
  
  
  '''
  정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.07ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	실패 (0.20ms, 10.4MB) -> 이건 왜 ?
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.11ms, 10.4MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.19ms, 10.2MB)
테스트 15 〉	통과 (0.11ms, 10.4MB)
테스트 16 〉	통과 (0.19ms, 10.3MB)
테스트 17 〉	통과 (0.06ms, 10.2MB)
테스트 18 〉	통과 (9.15ms, 10.2MB)
테스트 19 〉	통과 (3.44ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
  '''
