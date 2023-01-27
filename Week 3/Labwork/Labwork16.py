import math

n = int(input("Enter the number: "))
cnt = 0
for i in range(1, int(math.sqrt(2)) + 1):
    if n % i == 0:
        cnt += 1
if cnt != 2:
    print("Not prime")
else:
    print("Prime")
