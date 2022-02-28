# 무지성으로 풀었지만 길이가 고정이라 나쁘지 않은 방법이었음.
# 아예 사전 전체를 구해도 3000개 정도 원소

# 

def solution(word):
    answer = 0
    # 바로 떠오르는 방법은 반복문으로 경우의수 다 따져도 3천개 정도니까 그렇게 찾으면 되지 않을까 ?
    
    char = ["","A","E","I","O","U"]
    dictionary = set([])
    for a in char :
        for b in char:
            for c in char:
                for d in char :
                    for e in char :
                        dictionary.add(a + b+ c+ d + e)
    #print(dictionary)
    dictionary=list(dictionary)
    dictionary.sort()
    del dictionary[0]
    
    
    
    
    return dictionary.index(word)+1




# 다른 사람 풀이
# 등비 수열의 합으로 풀었다고 함.

def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer
