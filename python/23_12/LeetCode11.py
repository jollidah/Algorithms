# Containser With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        hList = list()
        for i, h in enumerate(height):
            hList.append((h, i))
        hList.sort(reverse=True)
        lp, rp, i, res = hList[0][1], hList[0][1], 1, 0
        while not (lp == 0 and rp == len(height) - 1):
            if lp > hList[i][1]:
                lp = hList[i][1]
                res = max(res, (rp - lp) * hList[i][0])    
            elif rp < hList[i][1]:
                rp = hList[i][1]
                res = max(res, (rp - lp) * hList[i][0])
            i += 1
        return res

# https://leetcode.com/problems/container-with-most-water/