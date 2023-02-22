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
    i = len(num1) - 1
    j = len(num2) - 1
    answer = ''
    carried = 0
    while i > -1 and j > -1:
        a = ord(num1[i]) - 48
        b = ord(num2[j]) - 48
        add = a + b + carried
        answer = chr((add % 2) + 48) + answer
        carried = 1 if add == 2 or add == 3 else 0
        i -= 1
        j -= 1
    while i > -1:
        a = ord(num1[i]) - 48
        add = a + carried
        answer = chr((add % 2) + 48) + answer
        carried = 1 if add == 2 or add == 3 else 0
        i -= 1
    while j > -1:
        b = ord(num2[j]) - 48
        add = b + carried
        answer = chr((add % 2) + 48) + answer
        carried = 1 if add == 2 or add == 3 else 0
        j -= 1
    answer = '' + answer if carried == 0 else '1' + answer
    return answer


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
