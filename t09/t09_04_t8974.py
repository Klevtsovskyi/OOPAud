N = int(input())
array = [int(x) for x in input().split()]

counter = {}
for i in range(N):
    x = array[i]
    if x in counter:
        counter[x][0] = i   # index
        counter[x][2] += 1  # count
    else:
        counter[x] = [i, x, 1]  # index, item, count

for index, item, count in sorted(counter.values()):
    if count > 1:
        print(item, end=" ")
