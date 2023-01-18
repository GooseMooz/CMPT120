inp = int(input("Enter a number: "))
if inp > 100:
    print('Greater than 100')
else:
    if inp > 10:
        print('Greater than 10 and <= 100')
    else:
        if inp > 0:
            print('Greater than 0 and <= 10')
        else:
            print('Equal or <= 0')
# ===============Other Way================== #
if inp > 0:
    if inp > 10:
        if inp > 100:
            print('Greater than 100')
        else:
            print('Greater than 10 and <= 100')
    else:
        print('Greater than 0 and <= 10')
else:
    print('Equal or <= 0')
