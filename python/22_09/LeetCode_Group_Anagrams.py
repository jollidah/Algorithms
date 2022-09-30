class Solution:
    def groupAnagrams(self, strs):
        strList = [sorted(list(strs[0]))]   # 입력된 각 스트링을 정렬한 값을 저장해둘 리스트 같은 anagram인지 확인하기 위한 도구
        res = [[strs[0]]]
        for i in range(1, len(strs)):
            isIn = False
            tmpData = sorted(list(strs[i])) # 리스트 속 하나의 스트링을 정렬해둔 데이터로 같은 anagram이 strList에 있는지 비교하기 위한 도구
            for t in range(len(res)):
                if tmpData == strList[t]:
                    res[t].append(strs[i])
                    isIn = True
                    break
            if not isIn:
                strList.append(tmpData)
                res.append([strs[i]])
        return res


s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

# https://leetcode.com/problems/group-anagrams/
