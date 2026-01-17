n = int(input())
fDigit = (n % 10)
sDigit = ((n % 100)-fDigit) // 10
tdigit = (n - (n % 100)) // 100
print(fDigit+sDigit+tdigit)