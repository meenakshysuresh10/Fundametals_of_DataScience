# Case Study 15: Likes Frequency Distribution
import pandas as pd

data = {
    'PostID': [201, 202, 203, 204, 205, 206, 207, 208],
    'Likes': [10, 15, 10, 20, 15, 10, 25, 20]
}
df = pd.DataFrame(data)
like_frequency = df['Likes'].value_counts().sort_index()
print("Frequency distribution of likes among posts:")
print(like_frequency)

# Case Study 16: Word Frequency in Customer Reviews
from collections import Counter
import string

data = {
    'ReviewID': [1, 2, 3, 4],
    'ReviewText': [
        "Great product, really loved it!",
        "Good quality, but too expensive.",
        "Amazing product, worth the price.",
        "Not bad, but expected better quality."
    ]
}
df = pd.DataFrame(data)
all_reviews = ' '.join(df['ReviewText'].str.lower())
all_reviews = all_reviews.translate(str.maketrans('', '', string.punctuation))
words = all_reviews.split()
word_freq = Counter(words)
print("Frequency distribution of words in customer reviews:")
print(word_freq)
