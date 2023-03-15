def remove_digits(s):
    ans = ''
    for i in range(len(s)):
        if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
            ans = ans + s[i]
    return ans


print(remove_digits('Ab a12 cDe#?'))
print(remove_digits('1234#?'))
print(remove_digits('1234'))


valid_pin = input("Enter your pin: ")


def is_valid_pin(s):
    if 3 < len(s) < 6:
        for i in range(len(s)):
            if s[i] != valid_pin[i]:
                return False
        return True
    else:
        return False


print(is_valid_pin('1234'))
print(is_valid_pin('01234'))
print(is_valid_pin('345@'))
print(is_valid_pin('123456'))
print(is_valid_pin('1 234'))
