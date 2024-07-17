from collections import defaultdict
from fractions import Fraction

def sum_probability():
    M = int(input("Enter the number of dice (M): "))
    N = int(input("Enter the number of sides on each die (N):"))

    # Dictation to store probabilities
    probabilities = defaultdict(Fraction)

    # Base case: one dice
    for i in range(1,N+1):
        probabilities[i]= Fraction(1,N)

    # Iterate for each additional die
    for _ in range(1, M):
        new_probability = defaultdict(Fraction)
        for sum_so_far in probabilities:
            for face in range(1, N+1):
                new_probability[sum_so_far + face] += probabilities[sum_so_far] / N
        probabilities = new_probability

    # Covert fractions to float for display
    probabilities = {k: float(v) for k,v in probabilities.items()}

    print(f"The probability of each possible sum of roll {M} number of {N}-sided diece are listed below:")
    return probabilities

simulation = sum_probability()
print(f"{simulation}")