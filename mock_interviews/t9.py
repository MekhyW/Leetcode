T9_CHARS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

trie = None

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

LETTER_TO_DIGIT = {}
for digit, letters in T9_CHARS.items():
    for letter in letters:
        LETTER_TO_DIGIT[letter] = digit

def insert_into_trie(word):
    node = trie
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_word = True

def search_in_trie(node, number, index, prefix, results):
    if index == len(number):
        if node.is_word:
            results.append(prefix)
        return
    digit = number[index]
    if digit not in T9_CHARS:
        return
    for char in T9_CHARS[digit]:
        if char in node.children:
            search_in_trie(node.children[char], number, index + 1, prefix + char, results)

def get_valid_t9_words(number: str, words: list[str]) -> list[str]:
    global trie
    if trie is None:
        trie = TrieNode()
        for word in words:
            insert_into_trie(word.lower())
    results = []
    search_in_trie(trie, number, 0, '', results)
    return results
