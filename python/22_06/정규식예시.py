import re
s = "2349iasdf"
res = re.search("i.s", s)           # type = <class 're.Match'>
print(res.group())                  # res.group()으로 출력해야 ias가 출력된다

s = 'hello-world-123-good-984'      # search는 하나만 찾지만 findall은 일치하는 모든 부분을 찾아준다
m = re.findall('[a-zA-Z]+',s)       # [a-zA-Z]는 모든 문자열을 뜻한다
print(m)


# {}울 이용해 반복이 되는 부분 찾기
s = '0aaa5'
m = re.search('a{3,4}', s)          # a{3,4}는 범위를 나타내는 정규식. a가 3번이상이고 4번 이하면 맞는 패턴으로 본다
print(m.group())                    # 출력결과 : aaa

s1 = '휴대전화에요.010-1234-9001'
m1 = re.search('[0-9]{2,3}-[0-9]{4}-[0-9]{4}', s1)  # 숫자 2~3개 + 숫자 4개 + 숫자 4개
print(m1.group())                   # 출력결과 : 010-1234-900
s2 = '중국집이에요.02-2940-7001'
m2 = re.search('[0-9]{2,3}-[0-9]{4}-[0-9]{4}', s2)  # 숫자 2_3개 + 숫자 4개 + 숫자 4개
print(m2.group())                   #출력결과 : 02-2940-7001


# ^ 시작 문자를 확인하기 위한 메타기호
s = '안녕하세요. 좋은 아침이에요'
m = re.search('^안녕', s)
print(m.group())        # 출력결과 : 안녕

s = '좋은 아침이에요.안녕하세요'
m = re.search('^안녕', s)
print(m)                # 출력결과 : None


# $ 마지막 문자를 확인하기 위한 메타기호
s = '지금은 즐겁게 있어요'
m = re.search('[ㄱ-힣]+요$', s)          # [ㄱ-힣] 은 한글일때만 일치하는 걸로 본다는 뜻
print(m.group())        # 출력 결과 : 있어요


# |를 활용해 여러 정규식을 묶어서 사용할 수 있다
s = 'There is a crow and bird'
m = re.findall('cro*w|bir+d', s)        # | 앞뒤로 정규식이 2개 있다
print(m)                                # 출력결과 : ['crow', 'bird']
