money = float(input("Money: "))
toonies = str(int(money // 2))
money = money - (money // 2) * 2
loonies = str(int(money // 1))
money = money - (money // 1)
money = int(money * 100)
quarters = str(money // 25)
money = money - (money // 25) * 25
dimes = str(money // 10)
money = money - (money // 10) * 10
nickels = str(money // 5)
money = money - (money // 5) * 5
penny = str(money)

print(toonies + " toonies, \n" + loonies + " loonies, \n" + quarters + " quarters, \n" + dimes + " dimes,")
print(nickels + " nickels, \n" + penny + " pennies.")
