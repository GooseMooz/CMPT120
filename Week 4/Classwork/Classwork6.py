import math

n = int(input("How many prime numbers do you want? "))
i = 0
cnt = 1.0
while i < n:
    while True:
        cnt += 1
        counter = 0
        for j in range(1, int(math.sqrt(cnt)) + 1):
            if cnt % j == 0:
                counter += 1
        if counter == 1:
            print(int(cnt))
            break
    i += 1
