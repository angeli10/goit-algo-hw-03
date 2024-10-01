import random


def get_numbers_ticket(min, max, quantity):
    number_list = [] 
    if min > max or min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    numbers = set()

    while len(numbers) < quantity:
        number = random.randint(min, max)
        numbers.add(number)
   
    return sorted(numbers)

m = get_numbers_ticket(3, 9, 7)
print(m)


# import random


# def get_numbers_ticket(min, max, quantity):
#     if min > max or min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
#         return []
    
#     numbers = random.sample(range(min, max + 1), quantity)
#     numbers.sort()
#     return numbers

# m = get_numbers_ticket(1, 20, 15)
# print(m)