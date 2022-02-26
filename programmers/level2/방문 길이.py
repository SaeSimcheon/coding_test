# 모든 방향에 대해서 일단 이동 시킨 다음 절댓값이 5를 넘는 것을 확인하고 
def solution(dirs):
    
    D={"L":[-1,0],"U":[0,1],"D":[0,-1],"R":[1,0]}
    print(D)
    
    point = [0,0]
    answer = 0
    trace=[] # 처음 지나는 경로인 경우 기록하고 매 반복마다 이전에 지난 경로인지 확인해 answer에 반영할지 결정한다.
    for i in dirs:
        way = [point[:]]
        point = [point[0] + D[i][0],point[1] + D[i][1]]
        flag =0
        if point[0] > 5 :
            point[0] =  5
            flag =1
        if point[0] < -5 :
            point[0] =  -5
            flag =1
        if point[1] > 5:
            point[1] =5    
            flag =1
        if point[1] < -5:
            point[1] =-5
            flag =1
        way.append(point[:]) # 경로의 시작점과 끝점을 기록하여 이전에 거친 기록이 있다면 flag를 1로 설정하여 answer를 더하지 않는다.
        
        if way in trace or way[::-1] in trace : # 시작점과 끝점을 구분하지 않으므로 두 점이 각각 시작점과 끝점이 되는 경우 모두를 trace에서 찾아야한다.
            flag = 1
        
        if flag == 0 :
            trace.append(way)
            answer +=1
        
    return answer
 
