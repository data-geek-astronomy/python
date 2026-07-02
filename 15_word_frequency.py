from collections import Counter

def word_frequency(text):
    words = text.lower().split()
    return dict(Counter(words))

if __name__ == "__main__":
    print(word_frequency("the quick brown fox the lazy fox"))
