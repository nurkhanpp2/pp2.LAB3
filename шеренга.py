a = [int(i) for i in input().split()]
n = int(input())
pos = 0
while pos < len(a) and a[pos] >= n:
    pos += 1
print(pos + 1)