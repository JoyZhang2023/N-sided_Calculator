import random

def roll_dice():
    M = int(input("Enter the number of dice (M): "))
    N = int(input("Enter the number of sides on each die (N) :"))

    total_sum = sum(random.randint(1,N) for _ in range(M))

    return total_sum

simulation1 = roll_dice()
print(f"The sum of one rolling outcome is : {simulation1}")