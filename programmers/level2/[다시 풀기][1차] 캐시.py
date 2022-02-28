# lru 가장 옛날에 사용된 것 이탈시킴.
# 딕셔너리를 통해서 풀었고, 딕셔너리 키에 있으면 hit로 없으면 miss로 뒀으며
# miss인 경우를 cache가 비어있는지에 따라서 다르게 처리해 주었다.
# 만약 hit가 된다면 해당 시행에서 다시 사용된 것이므로 0으로 초기화 해준다.
# 한 시행이 끝나면 캐시 안에 모든 key에 대하여 1씩 더해주어 캐시에 머문 기간을 나타내었다.
def solution(cacheSize, cities):
    
    if cacheSize == 0 :
        return len(cities) * 5
    cache = {}
    answer = 0
    for city in cities:
        city = city.lower()
        
        if city not in cache.keys():
            answer +=5
            if len(cache) < cacheSize :
                cache[city] =0
            else:
                del cache[max(cache,key=cache.get)] 
                cache[city] = 0
        else:
            cache[city] = 0
            answer +=1
        for i in cache.keys():
            cache[i]+=1
    
    return answer



# 다른 사람 풀이

def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time

# deque로 풀었고, 데크의 빠른 조회를 이용해서 조회가 되면 remove로 제거 하고 다시 append 하는 방식을 사용했다. 
# maxlen이라는 것을 지정해줌으로써 원소가 추가로 더해지면 자동으로 사라지게 하는 특성을 이용했다.
# https://skeo131.tistory.com/76
