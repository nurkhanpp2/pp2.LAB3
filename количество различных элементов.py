a = [int(i) for i in input().split()]
num_dist = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_dist += 1
print(num_dist)