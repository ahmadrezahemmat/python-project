import math

def moadeleh(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return ("دلتا منفی است، ریشه‌های موهومی دارد", delta, None, None)
    elif delta == 0:
        root = -b / (2 * a)
        return ("دلتا صفر است، یک ریشه واقعی دارد", delta, root, None)
    else:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        return ("دلتا مثبت است، دو ریشه واقعی دارد", delta, root1, root2)

def daryaft():
    a = float(input(" A   : "))
    b = float(input(" B   : "))
    c = float(input(" C   : "))
    return a, b, c

def zakhireh(filename, a, b, c, delta, rishe):
    with open(filename, 'w', encoding='utf-8') as file:  # تغییر اینجا: افزودن encoding='utf-8'
        file.write(f"moadeleh: {a}x^2 + {b}x + {c} = 0\n")
        file.write(f"delta: {delta}\n")
        if rishe[2] is not None:
            file.write(f"risheha: {rishe[1]} و {rishe[2]}\n")
        else:
            file.write(f"risheh: {rishe[1]}\n")

# اجرای برنامه
a, b, c = daryaft()
results = moadeleh(a, b, c)
zakhireh("quadratic_results.txt", a, b, c, results[1], results)

# چاپ پیام نهایی
print(f"  natayej: 'quadratic_results.txt'   {results[0]}")
