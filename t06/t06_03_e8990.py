string = input()

result = ""
for char in string:
    result += char
    if char in "aeiouy":
        result += char

print(result)
