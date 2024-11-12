values = input().split()
X, Y = int(values[0]), int(values[1])

count = 1
while count <= Y:
    print(count, end=' ')
    count += 1
    if count % X == 0:
        print()