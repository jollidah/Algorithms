import sys
import heapq

def main():
    inp = sys.stdin.readline
    check_dict, n_list = dict(), []
    for _ in range(int(inp())):
        n = int(inp())
        if n == 0:
            try:
                min_value = heapq.heappop(n_list)
                if -min_value in check_dict.keys() and check_dict[-min_value] != 0:
                    min_value = -min_value
                print(min_value)
                check_dict[min_value] -= 1
            except:
                print(0)
        else:
            if n in check_dict.keys():
                check_dict[n] += 1
            else:
                check_dict[n] = 1
            heapq.heappush(n_list, abs(n))

if __name__ == "__main__":
    main()
