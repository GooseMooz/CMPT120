import math
import random
a = random.randint(1, 100)
print("A = ", str(a))
b = random.randint(1, 100)
print("B = ", str(b))
c = random.randint(1, 100)
print("C = ", str(c))
d = (b ** 2) - 4 * a * c
if d > 0:
    x1 = -b + math.sqrt(d)
    x1 /= (2 * a)
    print('X1 = ' + str(x1))
    x2 = -b - math.sqrt(d)
    x2 /= (2 * a)
    print('X2 = ' + str(x2))
elif d < 0:
    print("ඞ")
else:
    x = -b / (2 * a)
    print('X = ' + str(x))
