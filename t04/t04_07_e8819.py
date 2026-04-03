n = int(input())

# count = 0
# for i in range(10**(n-1), 10**n):
#     if i % 2 == 0:
#         count += 1
# print(count)

if n == 1:
    print(4)
else:
    print(45 * 10**(n - 2))
