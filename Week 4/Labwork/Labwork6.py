n = int(input("Enter the number: "))

spaces = 0
for i in range(0, n):
    space = "  " * spaces
    print(space, end="")
    print("ඞ ", end="")
    for j in range(spaces + 1, n):
        print("ඞ " * 2, end="")
    print(space, end="")
    print("")
    spaces += 1
