import random

n = int(input("Enter the number of inputs: "))
ans = 0
max = -10000000000000000000
for i in range(0, n):
    inp = random.randint(-100, 100)
    if abs(inp) > max:
        ans = inp
        max = abs(inp)
print(ans)
