import sys

def solution():
    inp = sys.stdin.readline
    students_nums = [inp().rstrip() for _ in range(int(inp()))]
    limit = len(students_nums[0]) + 1
    for k in range(1, limit):
        saved_names = set()
        for student in students_nums:
            temp = student[len(student) - k: len(student)]
            if temp in saved_names:
                break
            else:
                saved_names.add(temp)
        else:
            print(k)
            exit(0)

if __name__ == "__main__":
    solution()
