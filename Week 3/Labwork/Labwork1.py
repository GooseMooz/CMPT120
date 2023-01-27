n = int(input("How many numbers you'll enter: "))
min = 100000000000000000000000
max = -10000000000000000000000
for i in range(0, n):
    inp = float(input("Enter number " + str(i + 1) + ": "))
    if inp < min:
        min = inp
    if inp > max:
        max = inp
print(min, max)
