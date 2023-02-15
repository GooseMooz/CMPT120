n = int(input("Enter the number: "))

for i in range(0, 2 * n):
    spaces = "  " * abs(n - i)
    print(spaces, end=" ")
    for j in range(1, n - abs(n - i) + 1):
        print(j, end=" ")
    print("")
