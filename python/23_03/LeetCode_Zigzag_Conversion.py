# Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        resList = [[] for _ in range(numRows)]
        p = 0
        d = 1
        if numRows == 1:
            return s
        for i in range(len(s)):
            resList[p].append(s[i])
            p += d
            if p == numRows:
                p = numRows - 2
                d = -1
            elif p == -1:
                p = 1
                d = 1
        res = ""
        for i in  range(numRows):
            res += "".join(resList[i])
        return res

# https://leetcode.com/problems/zigzag-conversion/description/
