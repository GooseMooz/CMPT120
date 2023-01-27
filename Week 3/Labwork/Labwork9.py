n = int(input("Enter a number: "))
cnt = 1
ans = 1
while cnt < n + 1:
    temp = cnt
    ans = ans * temp
    cnt += 1
print(ans)
