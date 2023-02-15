import random
import math

n1 = random.randint(50, 100)
n2 = random.randint(200, 300)

for i in range(n1, n2):
    cnt = 0
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        print(i)
