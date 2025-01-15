import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000:
        list = range(min, max)
        target = random.sample(list, quantity)
        return(sorted(target))
    else:
        target = []
        return(target)
lottery_numbers = get_numbers_ticket(1, 1200 , 4)

print("Ваші лотерейні числа:", lottery_numbers)