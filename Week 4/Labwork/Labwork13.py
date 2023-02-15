n = int(input("Enter the number: "))
n -= 1

for i in range(0, 2 * n + 1):
    spaces = "  " * abs(n - i)
    print(spaces, end=" ")
    for j in range(0, n - abs(n - i)):
        print(j + 1, end=" ")
    if i <= n:
        print(i + 1, end=" ")
    else:
        print(n - abs(n - i) + 1, end=" ")
    for j in range(n - abs(n - i), 0, -1):
        print(j, end=" ")
    print(spaces)
