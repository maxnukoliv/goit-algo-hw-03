import random

def get_numbers_ticket(min, max, quantity):
    if min >= max or quantity <= 0:
            target = []
            return(target)
    elif min >= 1 and max <= 1000 :
        list = range(min, max)
        target = random.sample(list, quantity)
        return(sorted(target))
    else:
        target = []
        return(target)

lottery_numbers = get_numbers_ticket(1000, 2, 3232)

print("Ваші лотерейні числа:", lottery_numbers)
