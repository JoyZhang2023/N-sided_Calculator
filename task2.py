import random

def possible_sum():
    M = int(input("Enter the number of dice (M): "))
    N = int(input("Enter the number of sides on each die (N):"))
    K = int(input("Enter the times of rolling die (K):"))

    results = []

    for _ in range(K):
        roll_once=[]
        for _ in range(M):
            roll_once.append(random.randint(1, N))
        results.append(roll_once)

    print(f"The possible results of roll {M} number of {N}-sided diece {K} times are listed below:")
    return results

simulation1 = possible_sum()
print(f"{simulation1}")