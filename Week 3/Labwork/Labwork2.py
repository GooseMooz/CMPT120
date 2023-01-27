import random

n = int(input("How many numbers you'll enter: "))
min = 100000000000000000000000
max = -10000000000000000000000
for i in range(0, n):
    inp = random.randint(5, 8)
    if inp < min:
        min = inp
    if inp > max:
        max = inp
print(min, max)
