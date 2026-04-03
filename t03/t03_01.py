n = int(input("n = "))
m = int(input("m = "))

# s = 0
# for i in range(m):
#     s += n  # s = s + n

s = 0
i = 0
while i < m:
    s += n
    i += 1

print(s)
