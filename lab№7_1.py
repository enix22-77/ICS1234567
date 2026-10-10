import random
text = input("Введіть рядок слів: ")
words = text.split()
print("Слова з великої літери:")
for word in words:
    if word[0].isupper():
        print(word)
random.shuffle(words)
print("Перемішані слова:")
print(" ".join(words))
