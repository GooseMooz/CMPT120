n = int(input("Enter the number: "))

spaces = n - 1
for i in range(0, n):
    space = "  " * spaces
    print(space, end="")
    for j in range(1, n - spaces):
        print(j, end=" ")
    print(i + 1, end=" ")
    for j in range(spaces + 1, n):
        print(n - j, end=" ")
    print(space, end="")
    print("")
    spaces -= 1
