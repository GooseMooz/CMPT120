n = int(input("Enter the number: "))

spaces = n - 1
for i in range(0, n):
    space = "  " * spaces
    print(space, end="")
    for j in range(spaces, n):
        print("ඞ ", end="")
    print("")
    spaces -= 1
