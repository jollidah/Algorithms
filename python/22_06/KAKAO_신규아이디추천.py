def solution(new_id):
    new_id = new_id.lower()
    for i in range(len(new_id) - 1, -1, -1):
        if not(new_id[i].isalpha() or new_id[i].isdecimal() or new_id[i] in["-", "_", "."]):
            new_id = new_id[:i] + new_id[i + 1:]
    if len(new_id) >= 2:
        for i in range(len(new_id) - 1, 0, - 1):
            if new_id[i] == "." and new_id[i - 1] == ".":
                new_id = new_id[:i] + new_id[i + 1:]
    if new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) >= 2:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if not new_id:
        new_id = "a"
    if len(new_id) >= 16:
        if new_id[14] == ".":
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
    answer = new_id
    return answer
  
  # https://programmers.co.kr/learn/courses/30/lessons/72410/solution_groups?language=python3
  
  
# 이 부분은 다른 분의 코드인데 정규식의 필요성을 느낄 수 있었다.
# https://software-creator.tistory.com/32

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
  

  
