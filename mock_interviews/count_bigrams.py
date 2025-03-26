def count_bigrams(words: list[str]):
    bigrams = {}
    for w1, w2 in zip(words[:-1], words[1:]):
        w1_bigrams = bigrams.setdefault(w1, {})
        w1_bigrams[w2] = w1_bigrams.get(w2, 0) + 1
    return bigrams
