# 주차 요금 계산기
# 일반적으로 입차 출차 한 쌍으로 되어 있고, 입차만 있는 경우에는 24시로 두고 계산
# stack 문제로 접근할 수 있지 않을까 ?
# 입차인 경우 stack에 쌓아두고 출차를 만난 경우 out -> 근데 이건 출차되는 기준이 균일 해야하는데 그렇지 않아서 안 됨.
# 입차 없는 출차는 없음


# 입차 기록 dict - 출차가 종료까지 되지 않는 경우는 마지막에 따짐.
# 입차 -> 출차가 오면 dict에서 삭제

# 누적 주차시간 기록 dict

# 딕셔너리에서 key 및 값을 아예 지우는 것 del로 그냥 하면 되나 ? -> 맞음.
'''
    putin["asd"] = 1
    print(putin.keys())
    del putin["asd"]
    print(putin.keys())
    dict_keys(['asd'])
    dict_keys([])
'''

import math

def solution(fees, records):
    
    putin = dict()
    cumsum_time = dict()
    for record in records :
        record = record.split(" ")
        time=record[0].split(":")
        minute = int(time[0])*60 +int(time[1])
        
        if record[2] == "IN":
            putin[record[1]] = minute
        else:
            
            if record[1] not in cumsum_time.keys():
                cumsum_time[record[1]] =  minute - putin[record[1]]
            else:
                cumsum_time[record[1]] +=  minute - putin[record[1]] # 출차 시점 - 입차 시점
            
            # 윗부분 cumsum_time[record[1]]+= 쓰고 싶으면 최초에는 0으로 초기화가 되어 있어야함.
            # 더하려니까 자꾸 에러 남
            
            del putin[record[1]]
            #print(record[1],cumsum_time[record[1]])
    # 입차만 있고 출차가 없는 케이스
    for key in putin.keys() :
        if key in cumsum_time.keys():
            cumsum_time[key]+= 23*60 + 59 -putin[key]
        else :
            cumsum_time[key]= 23*60 + 59 -putin[key]
    #print(cumsum_time)
    # 조건때문에 dict를 sort 해야하는데 ? 간단한 방법이 있을까 ?
    # 
    #print(sorted(cumsum_time.items()))
    cumsum_time=dict(sorted(cumsum_time.items()))
    # 자동차별 요금 계산
    answer = []
    for key,value in zip(cumsum_time.keys(),cumsum_time.values()):
        # 기본 시간보다 큰 경우와 작거나 같은 경우로 나눔
        #print(key,value,fees[0])
        if fees[0] >= value:
            answer.append(fees[1])# 작은 경우 기본 요금
        else:
            #print(value,math.ceil((value-fees[0])/fees[2]))
            answer.append(fees[1] +math.ceil((value-fees[0])/fees[2])*(fees[3]))
            
    
        
        
    
    # The end of records
    
    return answer
