import random


def decide(x):
    global neg_sum
    global neg_avg
    global sum
    global avg
    global pos_sum
    global pos_avg
    if x < 0:
        neg_sum += x
        neg_avg += x
        sum += x
        avg += x
    else:
        pos_sum += x
        pos_avg += x
        sum += x
        avg += x


pos_sum = 0.0
pos_avg = 0.0
neg_sum = 0.0
neg_avg = 0.0
sum = 0.0
avg = 0.0

read_1 = int(input("Input first integer: "))
if read_1 < 0:
    neg_sum += read_1
    neg_avg += read_1
    sum += read_1
    avg += read_1
else:
    pos_sum += read_1
    pos_avg += read_1
    sum += read_1
    avg += read_1

read_2 = int(input("Input second integer: "))
if read_2 < 0:
    neg_sum += read_2
    neg_avg += read_2
    sum += read_2
    avg += read_2
else:
    pos_sum += read_2
    pos_avg += read_2
    sum += read_2
    avg += read_2

read_3 = int(input("Input third integer: "))
if read_3 < 0:
    neg_sum += read_3
    neg_avg += read_3
    sum += read_3
    avg += read_3
else:
    pos_sum += read_3
    pos_avg += read_3
    sum += read_3
    avg += read_3

read_4 = int(input("Input fourth integer: "))
if read_4 < 0:
    neg_sum += read_4
    neg_avg += read_4
    sum += read_4
    avg += read_4
else:
    pos_sum += read_4
    pos_avg += read_4
    sum += read_4
    avg += read_4

read_5 = int(input("Input fifth integer: "))
if read_5 < 0:
    neg_sum += read_5
    neg_avg += read_5
    sum += read_5
    avg += read_5
else:
    pos_sum += read_5
    pos_avg += read_5
    sum += read_5
    avg += read_5

def_1 = random.randint(1, 100)
decide(def_1)
def_2 = random.randint(1, 100)
decide(def_2)
def_3 = random.randint(1, 100)
decide(def_3)
def_4 = random.randint(1, 100)
decide(def_4)
def_5 = random.randint(1, 100)
decide(def_4)

neg_avg /= 5
pos_avg /= 5
avg /= 10
print("Positive sum: " + str(pos_sum))
print("Positive avg: " + str(pos_avg))
print("Negative sum: " + str(neg_sum))
print("Negative avg: " + str(neg_avg))
print("Sum: " + str(sum))
print("Avg: " + str(avg))
