def compare(numerator, denominator):
    # Check if denominator is explicitly not zero
    return denominator != 0 and numerator / denominator == 0.5

a = int(input())
b = int(input())

print(compare(a, b))