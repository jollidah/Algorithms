class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        L = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]   # 해당하는 인덱스 에서의 최댓값을 저장하는 2차원 배열
        S = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]   # 최댓값을 최신화 하는 과정에서 어디에서 온 데이터인지 저장(0은 (-1,-1), 2는 (-1, 0), 1은 (0, -1))
        res = []
        for i in range(len(text1)):
            for t in range(len(text2)):
                if text2[t] == text1[i]:  # 값이 같은 경우 1을 추가
                    L[t + 1][i + 1] = L[t][i] + 1
                    S[t + 1][i + 1] = 0
                else:
                    L[t + 1][i + 1], S[t + 1][i + 1] = max([L[t][i], 0], [L[t][i + 1], 2], [L[t + 1][i], 1])    # max값은 각 리스트의 0번 인덱스가 기준이 된다.
        return L[len(text2)][len(text1)]
      
# https://leetcode.com/problems/longest-common-subsequence/
