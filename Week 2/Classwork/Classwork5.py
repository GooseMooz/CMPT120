inp = float(input("Enter your income: "))
tax = 0
# How to make it in 6 ifs?
tax += inp * 0.0506
if inp // 45654 > 1:
    tax += (inp - 45654) * 0.077
    if inp > 91310:
        tax += (inp - 91310) * 0.105
        if inp > 104835:
            tax += (inp - 104835) * 0.1229
            if inp > 127299:
                tax += (inp - 127299) * 0.147
                if inp > 172602:
                    tax += (inp - 172602) * 0.168
                    if inp > 240716:
                        tax += (inp - 240716) * 0.205
print('Your tax is: ' + str(tax))
