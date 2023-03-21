import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()
st = []

for i in range(n):
    if k == 0:
        st.append(s[i:])
        break
    else:
        while st and k > 0:
            if st[-1] < s[i]:
                st.pop()
                k -= 1
            else:
                break
        st.append(s[i])
print("".join(st) if k == 0 else "".join(st[:-k]))