f = open("output.txt", "w")
for i in range(1, 10):
    print(str(i) * i, file=f)
f.close()
