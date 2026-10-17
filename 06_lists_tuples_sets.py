fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.insert(1, "orange")
fruits.remove("banana")
print(fruits)
last = fruits.pop()
print("removed:", last)
print(fruits)

numbers = [5, 2, 9, 1, 7]
print("sum:", sum(numbers))
print("max:", max(numbers))
print("min:", min(numbers))
numbers.sort()
print("sorted:", numbers)
for n in numbers:
    print(n)

point = (4, 7)
x, y = point
print("x =", x, "y =", y)
print(point[0], len(point))

s = {1, 2, 3, 3, 2, 1}
print(s)
s.add(10)
print(s)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(a & b)
print(a - b)
print(set([10, 20, 10, 30]))
