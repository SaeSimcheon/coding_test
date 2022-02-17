
# 첫번째 시도 (런타임 에러가 남)

# 그 외의 알파벳은 소문자 -> 일단 전체 lower
# 첫 문자가 대문자 -> 전부 split 한 다음에 첫문자만 capital
# 대문자로 만드는 함수는 upper임.
# lower->split -> 별도의 함수를 만들어서 map -> list 할 것임
# 마지막에 join을 통해서 string으로 다시 만들어줌.



def make_first_upper(element):
    return element[0].upper()+ element[1:]


def solution(s):
    #print(s.lower())
    #print(make_first_upper("asdf"))
    s=s.lower()
    s=list(map(lambda x : make_first_upper(x), s.split(' ')))
    
    return " ".join(s)
  
# 생각에는 make_first_upper 함수에서 index로 합치는 과정에서 에러가 생기는듯 -> 아님


# 확인해보기 element[0] 이렇게 slicing 자체가 잘 못됨.
# 공백문자가 연속해서 나올 수 있는 조건때문에 에러가 나오는듯 split으로 쪼개면 공백을 무시하고 결과를 만들기 때문에
# 길이가 달라서 비교가 안 될 수 있음.




# 그 외의 알파벳은 소문자 -> 일단 전체 lower
# 첫 문자가 대문자 -> 전부 split 한 다음에 첫문자만 capital
# 대문자로 만드는 함수는 upper임.
# lower->split -> 별도의 함수를 만들어서 map -> list 할 것임
# 마지막에 join을 통해서 string으로 다시 만들어줌.

# 확인해보기 element[0] 이렇게 slicing 자체가 잘 못됨.
# 공백문자가 연속해서 나올 수 있는 조건때문에 에러가 나오는듯 split으로 쪼개면 공백을 무시하고 결과를 만들기 때문에
# 길이가 달라서 비교가 안 될 수 있음.





## 공백이 2개 들어가면 ''(아무 것도 없음)으로 list에 저장됨.
## print("1  3".split(" "))
## ['1', '', '3'] 이런 식으로


## 통과한 코드

def make_first_upper(element):
    if element =='': # 이 부분에서 원래 ''(아무 것도 없음)이 아니라 ' '(공백)으로 설정했었는데, split 함수가 공백이 2번들어가면 한 공백을 split의 결과가 되는 list에 ''(아무 것도 없음)
     # 으로 저장하기 때문에 map할 함수를 짤때 신경썼어야 했음.
        return element
    return element[0].upper()+ element[1:]


def solution(s):

    s=s.lower()
    s=list(map(lambda x : make_first_upper(x), s.split(' ')))
    
    return " ".join(s)


# D+1

def function(element):
    if element == '':
        return element
    else:
        return element[0].upper() + element[1:]
def solution(s):
    s=s.lower()
    answer = list(map(lambda x : function(x),s.split(" ")))
    return ' '.join(answer)
