inp = float(input("Enter your income: "))
tax = 0
if inp > 240716:
    tax += (inp - 240716) * 0.205
    tax += (240716 - 172602) * 0.168
    tax += (172602 - 127299) * 0.147
    tax += (127299 - 104835) * 0.1229
    tax += (104835 - 91310) * 0.105
    tax += (91310 - 45654) * 0.077
    tax += 45654 * 0.0506
else:
    if inp > 172602:
        tax += (inp - 172602) * 0.168
        tax += (172602 - 127299) * 0.147
        tax += (127299 - 104835) * 0.1229
        tax += (104835 - 91310) * 0.105
        tax += (91310 - 45654) * 0.077
        tax += 45654 * 0.0506
    else:
        if inp > 127299:
            tax += (inp - 127299) * 0.147
            tax += (127299 - 104835) * 0.1229
            tax += (104835 - 91310) * 0.105
            tax += (91310 - 45654) * 0.077
            tax += 45654 * 0.0506
print('Your tax is: ' + str(tax))