class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        h, w = len(matrix), len(matrix[0])
        resLength = h * w
        hp, wp = 0, 0
        for i in range(w):
            res.append(matrix[0][i])
        wp = w - 1
        while h != 0 and w != 0:   # 양수인 경우는 아래 + 왼쪽, 음수인 경우는 위 + 오른쪽 방향으로 순회 부호가 하나의 flag
            if h > 0:
                for i in range(1, h):   # 남은 높이만큼 이동 후 heightPtr도 이동
                    res.append(matrix[hp + i][wp])
                hp += h - 1
                for i in range(1, w):   # 남은 너비만큼 이동 후 weidthPtr도 이동
                    res.append(matrix[hp][wp - i])
                wp -= w - 1
                h -= 1
                w -= 1
                h *= -1
            else:
                h *= -1
                for i in range(1, h):
                    res.append(matrix[hp - i][wp])
                hp -= h - 1
                for i in range(1, w):
                    res.append(matrix[hp][wp + i])
                wp += w - 1
                h -= 1
                w -= 1
        return res[:resLength:]
# https://leetcode.com/problems/spiral-matrix/submissions/
