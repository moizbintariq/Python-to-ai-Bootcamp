for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(2, 11, 2):
    print(i)

for i in range(5, 0, -1):
    print(i)
print("go!")

for i in range(1, 11):
    print("7 x", i, "=", 7 * i)

total = 0
for i in range(1, 11):
    total += i
print("sum =", total)

number = 1234
digit_sum = 0
while number > 0:
    digit_sum += number % 10
    number = number // 10
print("sum of digits =", digit_sum)

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
