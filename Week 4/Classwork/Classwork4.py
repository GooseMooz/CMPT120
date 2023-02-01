i = 0
for i in range(4, -5, -1):
    for j in range(0, 5):
        if j - 4 <= i <= -j + 4:
            print('*', end='')
        print('*', end='')
    print()
    i += 1
