class Solution:
    def myPermutation(self, a, b):    # 중복 순열을 고려하되, 연산시간이 긴 나눗셈을 최대한 하지 않았다.
            res = 1
            div = 1
            tmp = a + b
            while tmp > b:
                res *= tmp
                tmp -= 1
            tmp = a
            while tmp:
                div *= tmp
                tmp -= 1
            return res // div


    def climbStairs(self, n: int) -> int:     
        res = 0
        if n % 2 == 0:              # 최대한 2칸씩 올라가는 경우부터 점점 1칸씩 올라가는 경우를 늘리고 각 케이스 별로 순열을 계산한다.
            a = n // 2
            b = 0
            while a > 0:
                res += self.myPermutation(a, b)
                a -= 1
                b += 2
            return res + 1
        else:
            a = n // 2
            b = 1
            while a > 0:
                res += self.myPermutation(a, b)
                a -= 1
                b += 2
            return res + 1
          
          
   # https://leetcode.com/problems/climbing-stairs/
