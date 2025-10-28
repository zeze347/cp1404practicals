"""
Word Occurrences
Estimate: 15 minutes
Actual:   23 minutes
"""
text = input("Text: ")
words = text.split()
word_occurrences = {}

for word in words:
    if word in word_occurrences:
        word_occurrences[word] += 1
    else:
        word_occurrences[word] = 1

sorted_words = sorted(word_occurrences.keys())
max_length = max(len(word) for word in sorted_words)
for word in sorted_words:
    print(f"{word:{max_length}} : {word_occurrences[word]}")