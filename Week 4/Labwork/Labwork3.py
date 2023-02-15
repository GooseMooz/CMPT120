n = int(input("Input the number: "))
mult = 1
for i in range(1, n + 1):
    spaces = "  " * (mult - 1)
    print(spaces, end="")
    for j in range(1 + mult - 1, n + 1):
        print(j * mult, end=" ")
    print("")
    mult += 1
