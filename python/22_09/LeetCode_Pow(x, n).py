class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:        # basecase
            return 1
        if n > 0:         # 양수일 경우
            if n % 2 == 0:
                return self.myPow(x ** 2, n // 2)   # 짝수인 경우
            else:
                return x * self.myPow(x ** 2, (n - 1) // 2)   # 홀수인 경우
        else:             # 음수일 경우
            if n % 2 == 0:
                return self.myPow((1 / x) ** 2, -n // 2)
            else:
                return 1/x * self.myPow((1 / x) ** 2, (-n - 1) // 2)
              
  # https://leetcode.com/problems/powx-n/
  
