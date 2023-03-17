# Zigzag Conversion

class Solution(object):
    def convert(self, s, numRows):
        res = [[] for _ in range(numRows)]
        reS = ""
        d = 1
        pos = 0
        if numRows == 1:
            return s
        for i in range(len(s)):
            if pos == numRows - 1:
                res[pos].append(s[i])
                d = -1
                pos = numRows - 2
            elif pos == 0 :
                res[pos].append(s[i])
                d = 1
                pos = 1
            else :
                res[pos].append(s[i])
                pos += d
        for i in range(numRows):
            reS += "".join(res[i])
        return reS

# https://leetcode.com/problems/zigzag-conversion/description/
