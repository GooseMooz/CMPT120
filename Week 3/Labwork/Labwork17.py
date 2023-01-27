sum_even = 0
sum_odd = 0
for i in range(10, 41):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(sum_even, sum_odd)
