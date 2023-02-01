cnt = 3
for i in range(3, -4, -1):
    spaces = ' ' * abs(i)
    stars = '*' * (7 - abs(i) * 2)
    numbers = ''
    for j in range(0, 7 - abs(i) * 2):
        numbers += str(abs(3 - j))
    print(spaces + numbers, end='')
    print()
