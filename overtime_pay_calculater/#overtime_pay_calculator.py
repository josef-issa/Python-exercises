#overtime_pay_calculator.py

hrs = input("Enter Hours:")
h = float(hrs)
str_h=str(h)

rate = input("Enter haw mach you get paid per hour:")
rate = float(rate)
str_rate = str(rate)

if h>=40:
    regular = 40 * rate
    overtime = (h-40)*(rate*1.5)
    total = regular + overtime
    print(total)
    
else:
    total = h * rate
    print(total)