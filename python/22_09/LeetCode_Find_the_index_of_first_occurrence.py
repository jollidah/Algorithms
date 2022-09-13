import re

class Solution:       # 정규표현식의 위력
    def strStr(self, haystack: str, needle: str) -> int:
        p = re.compile(needle)
        m = p.search(haystack) 
        if m != None:
            return m.start()
        else:
            return -1
          
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
