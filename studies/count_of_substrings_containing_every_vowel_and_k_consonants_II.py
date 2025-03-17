class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._atLeastK(word, k) - self._atLeastK(word, k + 1)
    
    def _atLeastK(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        valid_substrings = 0
        start = 0
        end = 0
        vowel_count = {}
        consonant_count = 0
        while end < n:
            char = word[end]
            if char in vowels:
                vowel_count[char] = vowel_count.get(char, 0) + 1
            else:
                consonant_count += 1
            while len(vowel_count) == 5 and consonant_count >= k:
                valid_substrings += n - end
                start_char = word[start]
                if start_char in vowels:
                    vowel_count[start_char] -= 1
                    if vowel_count[start_char] == 0:
                        vowel_count.pop(start_char)
                else:
                    consonant_count -= 1
                start += 1
            end += 1
        return valid_substrings