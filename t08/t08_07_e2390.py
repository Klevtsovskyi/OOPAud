def solve(n, lst):
    if n == 0:
        print(*lst)
        return

    for i in range(1, n + 1):
        if len(lst) > 0 and i > lst[-1]:
            continue
        lst.append(i)
        solve(n - i, lst)
        lst.pop()


n = int(input())
solve(n, [])
