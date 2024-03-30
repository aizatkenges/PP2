def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return "No solution"

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print("Number of chickens:", result[0])
print("Number of rabbits:", result[1])
