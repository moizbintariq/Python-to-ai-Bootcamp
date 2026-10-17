person = {"name": "Hina", "age": 19}
person["city"] = "Lahore"
person["age"] = 20
print(person)
del person["city"]
print("name" in person)
for key, value in person.items():
    print(key, "->", value)

text = "to be or not to be"
count = {}
for w in text.split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
print(count)
