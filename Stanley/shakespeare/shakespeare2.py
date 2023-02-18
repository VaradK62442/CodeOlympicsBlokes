from nltk import ngrams
import urllib.request
from collections import Counter
import string

data = ""
with urllib.request.urlopen("https://www.gutenberg.org/cache/epub/100/pg100.txt") as f:
    data = f.read().decode('utf-8')

words = data.split()
words = [word.translate(str.maketrans('', '', string.punctuation)).lower() for word in words if word != '']
words = [word for word in words if word != '']

ngram_counts = Counter(ngrams(words, 2))
twograms = ngram_counts.most_common(10)
twograms = [elt[0] for elt in twograms]

ngram_counts = Counter(ngrams(words, 3))
threegrams = ngram_counts.most_common(10)
threegrams = [elt[0] for elt in threegrams]

ngram_counts = Counter(ngrams(words, 4))
fourgrams = ngram_counts.most_common(10)
fourgrams = [elt[0] for elt in fourgrams]

ngram_counts = Counter(ngrams(words, 5))
fivegrams = ngram_counts.most_common(10)
fivegrams = [elt[0] for elt in fivegrams]

print(f'Bigrams:\n')
[print(elt) for elt in twograms]
print()

print(f'Trigrams:\n')
[print(elt) for elt in threegrams]
print()

print(f'Quadgrams:\n')
[print(elt) for elt in fourgrams]
print()

print(f'Quingrams:\n')
[print(elt) for elt in fivegrams]
print()