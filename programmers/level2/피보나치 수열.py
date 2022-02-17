# dynamic programming이 먼저 떠오름
# 내가 예전에 dfs나 재귀문은 어떻게 짰을까 ?

# given을 1씩 키워서 기준값만큼 달성했을때 f1_을 return 하도록 했음.
# 런타임 에러 나오는데 ? 7 10 13 14
# n = 10만으로 설정한 경우 maximum recursion depth 때문에 문제가 되는 것을 확인할 수 있었음.


# 첫번째 시도
# 재귀구문 이용해서 풀려고 했는데 포기하고 두번째 시도
def f(given,f0_,f1_,criteria):
    #print(given,f0_,f1_,criteria)
    if given == criteria:
        #print("here")
        return f1_
    return f(given+1,f1_,f0_+f1_,criteria)




# 두번째 시도 (통과)


def solution(n):
    
    f0 = 0
    f1 = 1
    f2 = 1
    for _ in range(2,n+1):
        f2 = f0+ f1
        f0 = f1
        f1 = f2
    answer= f2
    return answer%1234567


# 다른 사람들은 어떻게 풀었을까 ?
# 나처럼 재귀로 푼 사람 없음

def solution(n):
    f_list = [0,1]
    for i in range(2,n+1):
        f_list.append((f_list[i-2]%1234567+f_list[i-1]%1234567)%1234567)
    return f_list[-1]



cache = [-1]*100
def fibonacci(num):
    if num == 0: return 0
    if num == 1: return 1
    if cache[num] != -1: return cache[num]
    cache[num] = fibonacci(num-1) + fibonacci(num-2)
    return cache[num]


