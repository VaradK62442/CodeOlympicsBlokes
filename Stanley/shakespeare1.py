import urllib.request
import string

data = ""
with urllib.request.urlopen("https://www.gutenberg.org/cache/epub/100/pg100.txt") as f:
    data = f.read().decode('utf-8')

words = {}
for line in data.split("\n"):
    for word in line.replace("\r", "").split(" "):
        word = word.translate(str.maketrans('', '', string.punctuation)).lower()
        if word != '':
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

top_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
print([elt[0] for elt in top_words[:101]])