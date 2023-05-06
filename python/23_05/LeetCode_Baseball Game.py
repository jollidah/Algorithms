class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l=[]
        for i in ops:
            if i=="C":
                l.pop()
            elif i=="D":
                l.append(2*l[-1])
            elif i=="+":
                l.append(l[-1]+l[-2])
            else:
                l.append(int(i))
        return sum(l)
