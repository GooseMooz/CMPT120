inp = int(input('Enter number from 1 to 15: '))
out = (inp % 2) + (inp // 2 % 2) * 10 + (inp // 2 // 2 % 2) * 100 + (inp // 2 // 2 // 2 % 2) * 1000
print(out)
