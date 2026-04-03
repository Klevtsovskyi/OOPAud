n = int(input())

i = 1
n //= 10
while n > 0:
    i += 1
    n //= 10

print(i)
