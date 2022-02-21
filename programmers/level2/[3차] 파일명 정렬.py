# 헤드 기준으로 사전순 정렬
# 대소구분 안 함 -> lower나 upper 사용해서 일관성을 갖추어야함.
# 9 10 0011 012 13 014 앞의 0은 무시하기 -> 0 제거하고 sort
# 앞 두조건이 같은 경우 입력 순서 유지
# 먼저 떠오르는 것은 subgrouping임




import re
# 패턴이 앞이네

def solution(files):
    
    # 도중에 런타임 에러나는 케이스가 몇 개 있었는데, 조건중에 파일명 이름안에 점(\.)들어갈 수 있고, \-, \s 또한 head 쪽에서 고려해야한다는 것을 깨달았다.
    # grouping을 통해 정규표현식으로 해결하였다.
    #print(re.match("([a-zA-Z\.\-\s]+)([0-9]+).*",files[0]).group(1))
    
    s =  [[re.match("([a-zA-Z\.\-\s]+)([0-9]+).*",x.lower()).group(1),
          int(re.match("([a-zA-Z\.\-\s]+)([0-9]+).*",x.lower()).group(2)),x
          ]
          for x in files]
          
    
    s.sort(key = lambda x : (x[0],x[1]))
    answer = [i[2] for i in s]
    #answer = []
    return answer
