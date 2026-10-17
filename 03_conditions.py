num = -4

if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")


marks = 72
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("F")


n = 15
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")


year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
