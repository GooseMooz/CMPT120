ans = 0
cnt = 0
a = 1.0
b = 2.0
f1 = a * a - 2.0
f2 = b * b - 2.0
while abs(a - b) > 0.000001:
    ans = (a + b) / 2
    if ans**2 - 2 == 0.0:
        break
    elif (a**2 - 2) * (ans**2 - 2) < 0:
        b = ans
    else:
        a = ans

    print(a, ans, b)
print(ans)
