n = int(input("How many numbers you'll enter: "))
odd_sum = 0
odd_avg = 0
odd_cnt = 0
even_sum = 0
even_avg = 0
even_cnt = 0
all_sum = 0
all_avg = 0
for i in range(0, n):
    inp = float(input("Enter number " + str(i + 1) + ": "))
    if inp % 2 == 0:
        even_sum += inp
        even_cnt += 1
    else:
        odd_sum += inp
        odd_cnt += 1
    all_sum += inp
even_avg = even_sum / even_cnt
odd_avg = odd_sum / odd_cnt
all_avg = all_sum / n
print(even_sum, even_avg, odd_sum, odd_avg, all_sum, all_avg)
