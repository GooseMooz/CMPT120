amount = float(input("Savings: "))
rate = float(input("Interest rate: "))
time = float(input("Years passed: "))
total = str(amount + amount * rate * time)
print("Total: " + total)
