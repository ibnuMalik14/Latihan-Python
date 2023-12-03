sentence = input("Enter a sentence: ")
n = int(input("Enter a number: "))

words = sentence.split()
longer_words = []

for word in words:
    if len(word) > n:
        longer_words.append(word)

print(longer_words)