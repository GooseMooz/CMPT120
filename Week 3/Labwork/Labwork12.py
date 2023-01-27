n = int(input("Input the number: "))
ans = 0
cnt = 1
while cnt < n + 1:
    if cnt % 2 == 0:
        ans -= 1 / cnt
    else:
        ans += 1 / cnt
    cnt += 1
print(ans)
