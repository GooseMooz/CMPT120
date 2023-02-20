def to_str(number):
    out = ''
    j = 0
    cnt = 0
    temp = number
    if temp == 0:
        return '0'
    while j < temp:
        out = chr(number % 10 + ord('0')) + out
        j += (number % 10) * (10 ** cnt)
        cnt += 1
        number //= 10
    return out


def decimalToBinary(n):
    counter = 0
    temp = n
    while temp > 0:
        counter += 1
        temp //= 2

    temp = n
    out = ''
    for i in range(counter):
        out = to_str((temp % 2)) + out
        temp //= 2
    return out


def binaryAddition(num1, num2):
    if len(num1) <= len(num2):
        small = num1
        big = num2
    else:
        small = num2
        big = num1

    carried = False
    counter = 1
    out = ''
    for i in range(len(small)):
        if num1[-counter] == num2[-counter] == '0':
            if carried:
                counter += 1
                out = '1' + out
                carried = False
            else:
                counter += 1
                out = '0' + out
        elif num1[-counter] + num2[-counter] == '01' or num1[-counter] + num2[-counter] == '10':
            if carried:
                counter += 1
                out = '0' + out
            else:
                counter += 1
                out = '1' + out
        elif num1[-counter] == num2[-counter] == '1':
            if carried:
                counter += 1
                out = '1' + out
            else:
                counter += 1
                carried = True
                out = '0' + out
    if len(num1) == len(num2):
        if carried:
            out = '1' + out
        return out
    if carried:
        for i in range(len(big[:-counter]) + 1):
            if big[-counter] == '1':
                counter += 1
                out = '0' + out
            else:
                counter += 1
                out = '1' + out
                out = big[:-counter] + out
                return out
        out = '1' + out
        return out
    else:
        out = big[:-counter] + out
        return out


def binaryToDecimal(string):
    counter = 0
    out = 0
    for i in range(len(string)):
        out += (ord(string[-i - 1]) - 48) * (2 ** counter)
        counter += 1
    return out


n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
ans = n1 + n2

str1 = decimalToBinary(n1)
print("The binary representation of", n1, "is", str1)

str2 = decimalToBinary(n2)
print("The binary representation of", n2, "is", str2)

str3 = binaryAddition(str1, str2)
print("The binary addition of", n1, "and", n2, "is", str3)

n3 = binaryToDecimal(str3)
print("Converting the binary to decimal gives", n3)

if ans == n3:
    print("Since", ans, "==", n3, ", it seems we did good job.")
else:
    print("Since", ans, "!=", n3, ", something went wrong.")
