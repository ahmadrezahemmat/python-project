import random

def adad_kamel(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

def adad_tasadofi(num_count, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(num_count)]

def zakhireh_adad(numbers, filename):
    perfect_numbers = [num for num in numbers if adad_kamel(num)]
    print("Generated numbers:", numbers)
    print("Perfect numbers:", perfect_numbers)
    with open(filename, 'w') as file:
        for number in perfect_numbers:
            file.write(f'{number}\n')
    print(f"Perfect numbers saved to {filename}")

# تعریف پارامترها
num_count = 50
lower_bound = 100
upper_bound = 500        
filename = "perfect_numbers.txt"

# تولید اعداد تصادفی و ذخیره اعداد کامل
random_numbers = adad_tasadofi(num_count, lower_bound, upper_bound)
zakhireh_adad(random_numbers, filename)
