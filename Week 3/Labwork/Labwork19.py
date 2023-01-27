n = int(input("Enter the number: "))
max = -10000000000000000000000000000
for i in range(0, n):
    inp = float(input("Input your float: "))
    if inp > max:
        max = inp
print(max)
