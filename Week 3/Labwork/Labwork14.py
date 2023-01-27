min = -100000000000000000000
n = int(input("Enter the number: "))
cnt = 0
prev_number = 0
for i in range(0, n):
    inp = int(input("Enter number " + str(i + 1) + ": "))
    if inp > min:
        min = inp
    else:
        cnt += 1
if cnt > 0:
    print("No order")
else:
    print("Order")
