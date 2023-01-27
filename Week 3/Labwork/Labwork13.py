n = int(input("Enter the number: "))
cnt = 0
fib = 1
prev_fib = 1
print("1")
while cnt < n - 2:
    temp = fib + prev_fib
    fib = prev_fib
    prev_fib = temp
print(prev_fib)
