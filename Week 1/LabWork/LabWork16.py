inp = int(input("Input integer value from 0 to 255: "))

ans = (inp // 128) * (10 ** 7)
inp -= inp // 128 * 128

ans += (inp // 64) * (10 ** 6)
inp -= inp // 64 * 64

ans += (inp // 32) * (10 ** 5)
inp -= inp // 32 * 32

ans += (inp // 16) * (10 ** 4)
inp -= inp // 16 * 16

ans += (inp // 8) * (10 ** 3)
inp -= inp // 8 * 8

ans += (inp // 4) * (10 ** 2)
inp -= inp // 4 * 4

ans += (inp // 2) * (10 ** 1)
inp -= inp // 2 * 2

ans += inp

print("Answer in binary: ")
print(ans)
