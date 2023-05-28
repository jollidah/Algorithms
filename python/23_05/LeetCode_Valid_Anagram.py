class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        d_dict = dict()
        for word in s:
            s_dict[word] = s_dict.get(word, 0) + 1
        for word in t:
            d_dict[word] = d_dict.get(word, 0) + 1
        return s_dict == d_dict
