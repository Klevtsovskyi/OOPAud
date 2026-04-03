a, b, x, y, z = [float(d) for d in input().split()]

if (
        x < a and y < b or
        y < a and x < b or
        z < a and x < b or
        x < a and z < b or
        y < a and z < b or
        z < a and y < b
):
    print(1)
else:
    print(0)
