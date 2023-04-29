class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        
        for n in range(1, numRows):
            nextRow = [1]
            
            for m in range(n-1):
                nextRow.append(ans[n-1][m]+ans[n-1][m+1])
            
            nextRow.append(1)
            ans.append(nextRow)
            
        return ans
