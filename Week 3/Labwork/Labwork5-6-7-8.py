import random

n = random.randint(-5, 5)
min_odd = 100000000000000000000000
max_odd = -10000000000000000000000
min_even = 100000000000000000000000
max_even = -10000000000000000000000
if n > 0:
    for i in range(0, n):
        inp = random.randint(-10, 10)
        if inp > -1:
            if inp % 2 == 0:
                if inp > max_even:
                    max_even = inp
                if inp < min_even:
                    min_even = inp
            else:
                if inp > max_odd:
                    max_odd = inp
                if inp < min_odd:
                    min_odd = inp
    print(min_odd, max_odd, min_even, max_even)
else:
    print("* )----( *")
