def is_symmetric(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_symmetric(s[1:-1])


def replace(s, c, repl):
    if s == "":
        return ""
    elif s[0] == c:
        return repl + replace(s[1:], c, repl)
    else:
        return s[0] + replace(s[1:], c, repl)




print(is_symmetric("asddsa"))
print(is_symmetric("asdzxdsa"))
print(is_symmetric("1235311111111111111111111111111111111111144321"))

print(replace("123431", "1", "ASD"))
