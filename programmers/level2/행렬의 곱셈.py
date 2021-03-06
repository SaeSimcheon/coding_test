# 첫번째 풀이 (통과)
# transpose하지 않으려고 했는데 transpose 해서 저장해서 풀어버림
# zip을 제대로 사용할줄 몰라서 될때까지 결과를 중구난방으로 출력함.


def solution(arr1, arr2):
    
    for i in arr1:
        print(i)
    
    for j in zip(*arr2):    
        list(j)
    transpose=[ list(j) for j in zip(*arr2)]

    # 뒤에 곱해지는 행렬을 transpose 하지 않고, 쉽게 곱해지는 축을 리스트로 만드는 방법을 찾고 있었음. 
    # zip을 이용하면 손 쉽지 않을까 생각.
    # arr1의 col과 arr2의 row는 길이가 같으므로 한 iteration으로 수행할 수 있음.
    
    answer = []
    for index in range(len(arr1)):
        out = []
        for index2 in range(len(transpose)):
            a = []
            for i,j in zip(arr1[index],transpose[index2]):
                a.append(i*j)
            out.append(sum(a))
        answer.append(out)
            #zip(arr1[index],transpose[index2])
            #answer.append([i*j for i,j in zip(arr1[index],transpose[index2])])
    
    
    
    return answer



# D+1에 푼 흔적
# 같은 아이디어로 풀었음.
# 어제 반복문 하나를 추가해서 푼 것을 list comprehension을 통해서 해결하였음.
# arr2에 대한 zip을 두번째 반복문에 직접 넣어 사용함으로써 transpose한 matrix를 별도로 두지 않았음.

def solution(arr1, arr2):
    answer  = [ ]
    #for i in arr1:
    #    print(i)
        
    #for i in zip(*arr2):
    #    print(i)  
        
    for i in arr1:
        row = list()
        for j in zip(*arr2):
            element = [ii * jj for ii ,jj in zip(i,j)]
            row.append(sum(element))
        answer.append(row)
    
    
        
    return answer



'''
테스트 1 〉	통과 (2.31ms, 10.4MB)
테스트 2 〉	통과 (40.01ms, 11MB)
테스트 3 〉	통과 (44.10ms, 11MB)
테스트 4 〉	통과 (0.98ms, 10.1MB)
테스트 5 〉	통과 (29.93ms, 10.8MB)
테스트 6 〉	통과 (17.51ms, 10.8MB)
테스트 7 〉	통과 (0.83ms, 10.3MB)
테스트 8 〉	통과 (0.43ms, 10.1MB)
테스트 9 〉	통과 (0.36ms, 10.4MB)
테스트 10 〉	통과 (29.69ms, 10.6MB)
테스트 11 〉	통과 (3.00ms, 10.3MB)
테스트 12 〉	통과 (0.70ms, 10.2MB)
테스트 13 〉	통과 (21.94ms, 10.8MB)
테스트 14 〉	통과 (62.17ms, 11MB)
테스트 15 〉	통과 (12.11ms, 10.3MB)
테스트 16 〉	통과 (4.32ms, 10.5MB)
'''


# 다른 사람들은 어떻게 풀었을까 ?

#  - , - , - , 이도형 , Ezechiel_Kim 외 1 명

def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];
print("결과 : {}".format(productMatrix(a,b)));



## 반복문 총 3개로 풀었다는 점은 같고, 전체를 list comprehension을 사용했음.
## 출력을 통해서 구조를 확인하지 않아도 알 수 있다는 점에서 직관적일 수 있다.



# D+2

def solution(arr1, arr2):
    answer = []
    
    for i in arr1:
        one_out = []
        for j in zip(*arr2):
            a = sum([ii*jj for ii,jj in zip(i,j)]) # 원소 하나
            one_out.append(a) # 한 행을 만들기
        answer.append(one_out)
        
    
    return answer

