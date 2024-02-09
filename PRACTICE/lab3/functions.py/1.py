def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces

# Example usage:
grams_needed = float(input())
ounces_needed = grams_to_ounces(grams_needed)
print(ounces_needed)
