class Solution:
    def setZeroes(self, matrix) -> None:
        h = len(matrix)
        w = len(matrix[0])
        zeroList = []
        for i in range(h):
            for t in range(w):
                if matrix[i][t] == 0:
                    zeroList.append([i, t])
        while zeroList:
            tmpH, tmpW = zeroList.pop()
            for i in range(h):
                matrix[i][tmpW] = 0
            for i in range(w):
                matrix[tmpH][i] = 0

                
# https://leetcode.com/problems/set-matrix-zeroes/
