# 한 숫자를 연속적인 자연수로 표현하는 방법
# 자기 자신도 가능
# 그 값의 2로 나눈 몫까지만 찾으면 되는 것 같음.
# 가장 쉽게 떠올릴 수 있는 방법은 시작점 1, 2, 3, ,4 ,5 ... 그렇게 해서 연속하는 수를 계속 합해서 구하는 것.
# 그 값의 2로 나눈 몫까지만 더하면 답이 되는지 알 수 있음. 그 전에 끝나거나

# 이거 이분탐색 ?? dynamic programming / dfs bfs / greedy search
# 정렬 / 그래프 탐색

# 반복문 2개로 1부터 시작해서 n//2까지 탐색하는데 
# 안에 있는 반복문은 자기자신에서 시작해서 탐색하면 됨.

def solution(n):
    answer = 1 # 자기자신
    # range로 sum 될까? 됨.
    print(sum(range(0,10)))
    # 몫
    print(n//2)
    # 나머지
    print(n%2)
    for i in range(1,n // 2+1): # 2로 나눈 몫까지 시작점으로 삼기 위해서는 1을 더해야함.
        candidate =0
        for j in range(i,n//2+2): # 2로 나눈 몫의 경우에 적어도 그 값보다 1이 큰 경우까지 따지기 위해서는 n//2+2
            candidate += j
            if candidate > n : # 수를 더하는 도중에 만약 n 보다 크다면 안의 반복문을 멈춤.
                break
            if candidate == n : 
                print(i)
                answer+=1
                break
            
    
    
    return answer
    
    

# 다른 사람들은 어떻게 풀었을까 ?
# 내 코드와 차이는 나는 for 문을 2개로 짜고 내부에서 조건문을 통해서 이탈한 계획을 세운 반면
# 아래는 while을 통해서 매 반복마다 조건을 확인하였다.

def expressions(num):
    answer = 0
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            i += 1
        if s == num:
            answer += 1


    return answer

# 아래는 반복문 2개에 안쪽 반복문에서 조건문을 통해서 이탈조건을 만들었다는 점에서 나와 같지만, 각 반복문에서 num+1까지 따졌다는 점에서 차이가 있음.
# 정확히는 안쪽에서는 이탈조건 때문에 내가 짠 코드와 차이가 없지만, 바깥쪽 반복문에서 따지지 않아도 되는 숫자까지 따지기 때문에 상대적으로 오래걸릴 수 있음.

def expressions(num):

    count = 0

    for i in range(1,num+1):
        sum = 0
        for f in range(i, num+1):
            sum += f

            if sum == num:
                count += 1

            if sum > num :
                break

    return count


