payRate = 16.78
ssTax = 0.06
fiTax = 0.14
siTax = 0.05
uDuties = 10
insurance = 0
grossPay = 0

time = int(input("The amount of work hours this week: "))
dependants = int(input("The number of dependants: "))
if dependants > 2:
    insurance = 35

if time < 41:
    grossPay = payRate * time
else:
    grossPay = payRate * 40 + payRate * 1.5 * (time - 40)

print("Gross pay: " + str(grossPay))

ssTaxPay = grossPay * ssTax
print("Social Security Tax: " + str(ssTaxPay))

fiTaxPay = fiTax * grossPay
print("Federal Income Tax: " + str(fiTaxPay))

siTaxPay = siTax * grossPay
print("State Income Tax: " + str(siTaxPay))

takeHomePay = grossPay - ssTaxPay - fiTaxPay - siTaxPay - uDuties - insurance
print("Take-Home Pay: " + str(takeHomePay))
