import random

def high_low(numbers):
    highest = max(numbers)
    lower = min(numbers)
    return highest, lower

lottery = []
random_num = 10

for number in range(random_num):
    lottery.append(random.randint(1,100))

high_low(lottery)

print(high_low(lottery))
