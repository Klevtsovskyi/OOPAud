# Чи можна з літер слова 𝑎 скласти слово 𝑏, причому кожну літеру
# можна використати тільки один раз?
a = input()
b = input()

counter_a = {}
for c in a:
    if c in counter_a:
        counter_a[c] += 1
    else:
        counter_a[c] = 1

counter_b = {}
for c in b:
    if c in counter_b:
        counter_b[c] += 1
    else:
        counter_b[c] = 1

ok = True
for c in b:
    if c not in counter_a:
        ok = False
        break
    elif counter_a[c] < counter_b[c]:
        ok = False
        break

if ok:
    print("Ok")
else:
    print("No")
