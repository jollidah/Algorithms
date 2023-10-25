import sys
def Solution():
    inp = sys.stdin.readline
    n_list = [int(inp()) for _ in range(int(inp()))]
    numbers = [True for _ in range(max(n_list))]

    for idx in range(3, len(numbers) // 2, 2):
        if numbers[idx]:
            for i in range(2 * idx, len(numbers), idx):
                numbers[i] = False

    for n in n_list:
        if n == 4:
            print(1)
            continue
        cnt = 0
        for prime_num in range(3, n // 2 + 1, 2):
            if numbers[prime_num] and numbers[n - prime_num]:
                cnt += 1
        print(cnt)

if __name__ == "__main__":
    Solution()
