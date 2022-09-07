from collections import deque       # 덱을 가져오는 법을 까먹었다 주의하자

class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()
        inc = ["(", "[", "{"]
        dec = [")", "]", "}"]
        for char in s:
            if char in inc:
                dq.append(char)
            else:
                try:
                    if dq.pop() != inc[dec.index(char)]:  # 만약 닫는 기호가 나오면 dec 리스트에서 해당하는 인덱스를 이용해 값을 찾는다
                        return False
                except:                   # 예외처리를 이용해 False값에서 인덱스 에러를 방지한다
                    return False
        if dq:
            return False
        else:
            return True
# https://leetcode.com/problems/valid-parentheses/
