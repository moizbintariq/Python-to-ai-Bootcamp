word = "Bootcamp"
print(word[0])
print(word[-1])
print(word[2:5])
print(word[:4])
print(word[4:])
print(word[::-1])
print(len(word))

text = "   python to ai   "
print(text.strip())
print(text.title())
print(text.upper())
print(text.lower())
print(text.replace("ai", "AI"))
print(text.strip().split(" "))

sentence = "i love learning python"
print(sentence.count("o"))
print(sentence.find("love"))
print(sentence.startswith("i"))
print("python" in sentence)

vowels = 0
for letter in "programming":
    if letter in "aeiou":
        vowels += 1
print("vowels:", vowels)

w = "madam"
if w == w[::-1]:
    print(w, "is a palindrome")
else:
    print(w, "is not a palindrome")
