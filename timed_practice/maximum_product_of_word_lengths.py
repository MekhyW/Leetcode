from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lens = [0] * n
        for i in range(n):
            word = words[i]
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            masks[i] = mask
            lens[i] = len(word)
        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (masks[i] & masks[j]) == 0:
                    product = lens[i] * lens[j]
                    if product > max_product:
                        max_product = product
        return max_product