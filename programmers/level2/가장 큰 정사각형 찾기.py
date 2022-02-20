# 번거로운 방법이 먼저 떠오르니까 시도 하기 꺼려짐
# 무슨 알고리즘하고 관련히 있는걸까?

# 정사각형 찾아내기
# 시작점을 찾아서 정해진 방향만큼 이동하면 됨
# 짧은 변의 제곱이 가능한 최댓값
# 짧은 변부터 시작해서 1씩 줄여가면서 그런 넓이를 갖는 정사각형이 존재하는지 찾기
# cnn 하는 것처럼 filter를 사용해서 이동시키면 어떨까? 


# 보류
#def filter(size,point,obj):
    # point로부터 가로로 원하는 길이만큼 확인 (1)
    # point로부터 세로로 원하는 길이까지 row를 이동시키며 (1)을 수행.
    #for i in 


    
def solution(board):
    answer = 1234
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(i,j)
    
    return answer
  
