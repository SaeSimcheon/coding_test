# 첫번째 시도 (통과)
# 이거 아래로 내려가면서 기록하는거 아닌가 ?
# 1235
# 5(5)6(5)7(5)8(3)
# 10 11 12 11
# 4(12) 3(12) 2(11) 1(12)
# 그때그때 바로 이전의 같은 열의 원소 제외하고 최댓값을 선택해서 더해 내려가면 됨.

def solution(land):
    answer = 0
    
    for i in range(1,len(land)):
        for index,j in enumerate(land[i]):
            land[i][index]=land[i][index] + max(land[i-1][:(index)] + land[i-1][(index+1):])

    return max(land[len(land)-1])
    
    
# dynamic programming ?
# 메모이제이션 ?
# 기억 안 남... 공부하기 - legacy
