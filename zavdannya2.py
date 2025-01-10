import random

def get_numbers_ticket(min, max, quantity):
    list = range(min, max)
    target = random.sample(list, quantity)
    return(target)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)