def is_armstrong(number):
    digits = str(number)
    n = len(digits)
    total = sum(int(d) ** n for d in digits)
    return total == number
num = int(input("Enter a positive integer: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")