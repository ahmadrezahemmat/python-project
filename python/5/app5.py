import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sinus(x, n):
    sine = 0
    for i in range(n):
        term = ((-1)**i) * (x**(2*i+1)) / factorial(2*i+1)
        sine += term
    return sine

# خواندن مقدار x و n از کاربر
x = float(input("  x   : "))
n = int(input("   n   : "))

# محاسبه سینوس x
result = sinus(x, n)
print(f" sinx            : {result}")
