N = int(input())
start = 1
end = 3


for line in range(0, N):
    for count in range(start,end + 1):
        print(count, end=' ')
    start = end + 2
    end = end + 4
    print('PUM')