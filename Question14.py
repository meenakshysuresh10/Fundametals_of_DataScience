import string
from collections import Counter

# Open and read the file
with open('sample_text.txt', 'r') as file:
    text = file.read()

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Split into words
words = text.split()

# Count word frequencies
word_freq = Counter(words)

# Display word frequencies
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
