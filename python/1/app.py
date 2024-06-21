def maghsum(num1, num2):
    # پیدا کردن حداقل از دو عدد برای محدود کردن دوره حلقه
    min_number = min(num1, num2)
    # لیستی برای ذخیره مقسوم علیه‌های مشترک
    common_divisors = []

    # حلقه از 1 تا حداقل عدد برای یافتن مقسوم علیه‌های مشترک
    for i in range(1, min_number + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)
    
    return common_divisors

# مثال برای استفاده از تابع
result = maghsum(12, 18)
print(result)
