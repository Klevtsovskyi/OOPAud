s = input()

res = ""
p = ""
for c in s:
    if c != p:
        res += c
    p = c

print(res)
