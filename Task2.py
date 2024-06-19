#Task2a

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 32, 43, 54, 65, 76, 87, 98]

def db_number(num):
    if num % 2 == 0: 
        return num * 2 
    else:
        return num  

db_e_numbers = list(map(db_number, numbers))
print(1, db_e_numbers) 

#Task2b
import math

numbers = [-9, 0, 4, 9, 16, 25, -25, 32, -7, 9.3333]

p_numbers = list(filter(lambda x: x > 0, numbers))
sr = list(map(lambda x: math.sqrt(x), p_numbers))

print(2, sr)


