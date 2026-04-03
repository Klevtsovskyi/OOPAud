s = input()

count = 0
for c in s:
    if c in "AIOUEY":
        count += 1

print(count)
