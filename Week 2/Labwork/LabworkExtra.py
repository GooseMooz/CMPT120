letterCount = 26
letter = input("Enter letter: ")
steps = int(input("Enter amount of steps: "))
steps %= 26
let_int = ord(letter) - 96
let_int += steps
let_int %= 26

print(chr(let_int + 96))
