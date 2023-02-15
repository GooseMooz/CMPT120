cnt = 0
num = 1
while cnt < 3:
    svm = 0
    num += 1
    for i in range(1, int(num / 2) + 2):
        if num % i == 0:
            svm += i
    if svm == num:
        cnt += 1
        print(num)
