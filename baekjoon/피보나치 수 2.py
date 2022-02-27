# 자료 입력 유의해야 했고, 제출 방식이 함수를 정의하여 이루어지지 않아도 됨.


n=int(input())
F= [0,1]
    
for i in range(2,n+1):
    F.append(F[i-1] + F[i-2])
print(F[n])
