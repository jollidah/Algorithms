from queue import Queue

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = Queue()
        res = []
        remainNum = n - 1
        if n == 0:        # n이 1일때 예외처리
            return ["()"]
        q.put((remainNum, ["("], 1))    # 큐의 시작점
        while not q.empty():
            remainNum, recentString, closeNum = q.get()           # remainNum은 남아있는 "(" 의 갯수를 나타내고
            if remainNum == 0:                  # closeNum은 내가 다시 닫아야할 ")"의 갯수를 나타낸다
                recentString += ")" * closeNum
                res.append("".join(recentString))                 # 모두 0이 되면 res 리스트에 넣는다
            else:
                if closeNum > 0:
                    q.put((remainNum, recentString + [")"], closeNum - 1))        # ")"로 닫는 경우
                if remainNum > 0:
                    q.put((remainNum - 1, recentString + ["("], closeNum + 1))    # "("를 추가하는 경우 닫아야할 괄호가 하나 더 생기므로 closeNum도 1을 더한다.
        return res
      # https://leetcode.com/problems/generate-parentheses/
