# 첫번째 시도 

# arr에 있는 모든 원소의 최소인 공배수를 찾아야함.
# 공배수란 그 원소로 나누어지는 공통인 수를 말함. 
# 수를 연속해서 나누어 찾고 싶은데 안 되나 -> 수를 어디까지 키워야하는지 모르겠음.
# 적어도 있는 수를 다 곱한 수까지만 하면 되지 않을까 ?
# 이런 방식도 가능할 것 같은데, arr 첫 원소부터 끝까지 자신보다 뒤에 있는 원소들을 나누어지는 것들을 전부 나누고
# 정답에 곱함.
# 안 나누어지는 수는 그대로 유지
# 딱 한 번 확인으로 구할 수 있음
# pop을 위해서 미리 정렬함.
def solution(arr):
    
    answer = 1
    
    arr.sort(reverse = True)
    while True:
        this_time=arr.pop()
        print(arr)
        if len(arr) == 0 :
            answer *=this_time
            break
        for i in range(len(arr)):
            if arr[i] % this_time ==0:
                arr[i] //=this_time
            else:
                continue
        answer *=this_time
            
    return answer
    
# 두번째 시도
# 예제 통과 못함
# 2부터 가장 큰 수까지 반복해서 순회하여 arr를 수정하고 전체 합이 길이와 같아졌을때 끝난다고 생각했음.
    
    
def solution(arr):
    end=max(arr)+1
    answer =1
    while sum(arr) != len(arr):
        flag = 0
        for i in range(2,end):
            for index,j in enumerate(arr):
                if j % i == 0:
                    arr[index] //= i
                    answer *= i
                    break
            if flag == 1:
                break
            
    return answer
    
    
# while 반복문은 횟수 정해서 디버깅 하기



# 세번째 시도 (통과는 했지만 절대 좋은 풀이는 아님)



# arr 전체를 반복해서 1부터 순회해서 나눠서 결국 전부 1만 남게 만들면 되지 않을까
# 가장 큰 수
def solution(arr):
    answer= 0
    obj = max(arr)
    flag=0
    n = 0
    while True: 
        flag = 0
        for i in arr:
            if obj % i !=0:
                flag = 1
                break
        if flag == 1:
            obj+=1
            continue
        else:
            answer = obj
            break
    return answer
