line = int(input())

for count in range(1, line + 1):
    print(count, (count**2), ((count**2) * count))
    print(count, (count**2) + 1, (((count**2) * count) + 1))