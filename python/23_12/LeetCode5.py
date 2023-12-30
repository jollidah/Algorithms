# Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for dt in range(2):
            for i in range(len(s)):
                lp, rp = i, i + dt
                print(lp, rp)
                while lp >= 0 and rp < len(s):
                    if s[lp] != s[rp]:
                        break
                    lp -= 1
                    rp += 1
                lp += 1
                rp -= 1
                if len(res) <= rp - lp:
                    res = s[lp : rp + 1]

        return res

# https://leetcode.com/problems/longest-palindromic-substring/description/