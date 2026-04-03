def C(n, k):
    if k == 0 or n == k:
        return 1
    return C(n - 1, k - 1) + C(n - 1, k)


N = int(input())
for n in range(N):
    for k in range(n + 1):
        print(C(n, k), end=" ")
    print()
