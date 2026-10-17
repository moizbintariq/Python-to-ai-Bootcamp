name = "Hina"
age = 19
height = 5.4
is_student = True
nothing = None

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(nothing, type(nothing))

score = 50
score = score + 10
print("Score:", score)

age_text = "19"
age_number = int(age_text)
print("Next year:", age_number + 1)

print(int("42") + 8)
print(float("3.5") * 2)
print(str(100) + " marks")
print(int(9.99))
print(bool(0), bool(""), bool("hi"))

count = 1
while count <= 5:
    print("count =", count)
    count += 1

n = 5
while n > 0:
    print(n)
    n -= 1
print("Blast off!")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("odd:", i)

for i in range(50, 100):
    if i % 7 == 0:
        print("first multiple of 7 after 50 is", i)
        break
