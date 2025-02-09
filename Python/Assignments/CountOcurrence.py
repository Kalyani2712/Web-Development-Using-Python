from collections import Counter

string = "To change the overall look of your document. To change the look available in the gallery"
words = string.lower().replace(".", "").split()
word_count = Counter(words)

print(word_count)
