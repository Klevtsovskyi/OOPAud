s = input()

count = 0
word = ""
for c in s:
    if c.isalnum():
        word += c
    elif word:
        count += 1
        word = ""
if word:
    count += 1

print(count)
