i = 0
while i < 5:
    stars = '*' * (5 - i)
    spaces = ' ' * i
    print(spaces + stars, end='')
    print()
    i += 1
