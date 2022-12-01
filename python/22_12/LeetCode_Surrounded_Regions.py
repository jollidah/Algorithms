from queue import Queue

class Solution:
    def solve(self, board):
        h = len(board)
        w = len(board[0])
        q = Queue()   # queue for DFS
        isVisit = [[False for _ in range(w)] for t in range(h)]
        dirList = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(w - 1):      # 바깥쪽에 있는 "O"를 찾아 큐에 put 
            if board[0][i] == "O":
                q.put([0, i])
        for i in range(h - 1):
            if board[i][w - 1] == "O":
                q.put([i, w - 1])
        for i in range(w - 1, 0, -1):
            if board[h - 1][i] == "O":
                q.put([h - 1, i])
        for i in range(h - 1, -1, -1):
            if board[i][0] == "O":
                q.put([i, 0])
        while not q.empty():    # 큐에 아무것도 없을 때까지 진행
            y, x = q.get()
            isVisit[y][x] = True  # 방문했는지 확인
            for i in range(4):
                nextY = y + dirList[i][0]
                nextX = x + dirList[i][1]
                if 0 < nextY < h - 1 and 0 < nextX < w - 1 and board[nextY][nextX] == "O":  
                    if not isVisit[nextY][nextX]:
                        q.put([nextY, nextX])
        for i in range(1, h - 1):
            for t in range(1, w - 1):
                if board[i][t] == "O" and not isVisit[i][t]:    # 바깥쪽에서 방문한 적이 없는 "O" 제거
                    board[i][t] = "X"
                    
# https://leetcode.com/problems/surrounded-regions/
