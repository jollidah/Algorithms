class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ran = collections.Counter(ransomNote)
        dict_maz = collections.Counter(magazine)

        for key, value in dict_ran.items():
            if key not in dict_maz or value > dict_maz[key]:
                return False
            
        return True
