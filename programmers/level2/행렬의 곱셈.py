# 첫번째 풀이
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
