ans = 0
cnt = 0
a = 1.0
b = 2.0
f1 = a * a - 2.0
f2 = b * b - 2.0
if a * b < 0:
    ans = (a + b) / 2
    b = ans
    if cnt % 2 == 0:
        b = ans
    if cnt % 2 == 1:
        a = ans
