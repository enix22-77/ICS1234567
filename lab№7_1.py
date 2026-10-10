import random
text = input("Введіть рядок слів: ")
words = text.split()
print("Слова, що починаються з великої літери:")
for word in words:
    if word and word[0].isupper():
        print(word)
random.shuffle(words)
print("Слова у випадковому порядку:")
print(" ".join(words))
