text = input()
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y"]
for s in vowels:
    text = text.replace(s, "")
print(text)
