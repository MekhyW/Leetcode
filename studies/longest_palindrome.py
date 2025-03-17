class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) == 1):
            return s
        longest_palindrome, maxlen = s[0], 0
        for index in range(len(s)):
            for i in range(index+1):
                if index-i > maxlen:
                    substring = s[i:index+1]
                    if substring[0] == substring[-1]:
                        if substring == substring[::-1]:
                            longest_palindrome = substring
                            maxlen = index-i
        return longest_palindrome