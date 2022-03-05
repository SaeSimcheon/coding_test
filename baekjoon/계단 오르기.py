import sys
#sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline())



data=[int(sys.stdin.readline()) for _ in range(N)]


def solution():
    F = []
    if N <=2:
        print(sum(data))
        return
    F.append(data[0]) # 첫번째
    F.append(data[0]+data[1]) # 두번째

    flag = 0
    if max(F[0],data[1]) == data[1]:
        flag =1
    F.append(max(F[0],data[1])+ data[2])

    for i in range(3,N):
        pre2=F[i-2]
        pre3=F[i-3]
        F.append(max(pre2+ data[i],pre3+data[i-1]+data[i]   ))
    print(F[N-1])
solution()


# 앞의 세 항은 예외로 두고 마지막 항을 기준으로 2개 전항 3개 전항에서 규칙이 있다는 것을 발견했고, 각각으로부터 발생할 수 있는 값이 
# F.append(max(pre2+ data[i],pre3+data[i-1]+data[i]   )) 
