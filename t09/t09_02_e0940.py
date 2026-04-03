N = int(input())
array = [int(x) for x in input().split()]

counter = {}
for x in array:
    if x in counter:
        counter[x] = counter[x] + 1
    else:
        counter[x] = 1

for key, value in counter.items():
    if value > N // 2:
        print(key)
        break
else:
    print(-1)
