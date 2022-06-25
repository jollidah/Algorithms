class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      # 이중 반복문을 통해 시작점 이후 중복된 단어가 나올 경우 반복문을 중단하는 식으로 진행
        maxValue = 0                                        # 그 중 최댓값을 리턴한다
        for i in range(len(s)):
            tmpValue = 0
            res = []
            for t in range(i, len(s)):
                if s[t] in res:
                    break
                else:
                    res.append(s[t])
                    tmpValue += 1
            if maxValue < tmpValue:
                maxValue = tmpValue
        return maxValue

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
