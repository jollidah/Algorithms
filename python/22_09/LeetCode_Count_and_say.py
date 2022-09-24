class Solution:
    def countAndSay(self, n: int):
        if n == 1:        # IndexError를 방지하기 위한 예외처리
            return "1"
        if n == 2:
            return "11"
        else:
            res = []
            data = self.countAndSay(n - 1)
            ex_data = data[0]
            cnt = 1
            for i in range(len(data) - 2):  # 마지막에서 2번째 인덱스는 다르게 처리 해야 해서 len(data) - 2를 한 후에 예외처리를 따로 했다.
                if data[i] == data[i + 1]:
                    cnt += 1                # 다음 인덱스가 같다면 cnt를 1만큼 늘린다.
                else:
                    res.append(str(cnt))
                    res.append(str(ex_data))
                    ex_data = data[i + 1]
                    cnt = 1

            if data[len(data) - 2] == data[len(data) - 1]:      # 마지막 인덱스에 대한 예외 처리
                cnt += 1
                res.append(str(cnt))
                res.append(str(data[len(data) - 2]))
            else:
                res.append(str(cnt))
                res.append(str(data[len(data) - 2]))
                res.append(str(1))
                res.append(str(data[len(data) - 1]))
            return "".join(res)

# https://leetcode.com/problems/count-and-say/
