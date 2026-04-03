def is_prime(k):
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True


n = int(input())
for j in range(n, n * 2 + 1):
    if is_prime(j) and is_prime(j + 2):
        print(j, j + 2)
