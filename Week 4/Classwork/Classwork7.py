import random
spaces = 0
for i in range(0, 5):
    if spaces >= 4:
        for k in range(i, 5):
            print('_' * spaces + '*')
        break
    else:
        print('_' * spaces, end='')
        for j in range(0, 5 - spaces):
            rand = random.randint(0, 1)
            if rand == 0:
                print("*", end='')
                spaces += 1
                if spaces >= 4:
                    print("*", end='')
                    break
            else:
                if i == 4:
                    print("*" * (5 - spaces))
                    break
                else:
                    print("*", end='')
                    break
        print('')
