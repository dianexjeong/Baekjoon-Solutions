import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #", end="")
    print(i + 1, end="")
    print(":", a, "+", b, "=", a + b)
