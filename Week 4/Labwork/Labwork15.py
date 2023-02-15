n = int(input("Enter the number: "))

for i in range(1, 2 * n):
    spaces = "  " * (abs(n - abs(n - i)))
    print(spaces, end=" ")
    for j in range(0, abs(n - i)):
        print(j + 1, end=" ")
    print(abs(n - i) + 1, end=" ")
    for j in range(abs(n - i), 0, -1):
        print(j, end=" ")
    print(spaces)
