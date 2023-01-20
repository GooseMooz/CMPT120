prAmount = float(input())
time = int(input())
total = float(0)
rate1 = 0.025
rate2 = 0.02
rate3 = 0.015
rate4 = 0.01
if prAmount <= 0:
    print("error #c0000001d")
else:
    if prAmount > 1000:
        if prAmount > 10000:
            if prAmount > 100000:
                total = prAmount * (1.0 + rate4 * time)
            else:
                total = prAmount * (1.0 + rate3 * time)
        else:
            total = prAmount * (1.0 + rate2 * time)
    else:
        total = prAmount * (1.0 + rate1 * time)

print("Total: ", str(total))
