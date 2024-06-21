def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

def sum_factorial(number):
    sum_of_factorials = 0
    original_number = number

    while number > 0:
        digit = number % 10
        sum_of_factorials += factorial(digit)
        number //= 10

    return sum_of_factorials == original_number

# ورودی گرفتن از کاربر
input_number = int(input(" lotfan adad ra vared konid   : "))
result = sum_factorial(input_number)

if result:
    print(f"  majmu faktoeiel adad {input_number} ba khod adad barabar ast    .")
else:
    print(f"  majmu faktoeiel adad {input_number} ba khod adad barabar nist    .")
