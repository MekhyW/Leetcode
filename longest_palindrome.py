class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) == 1):
            return s
        longest_palindrome, maxlen = s[0], 0
        for index in range(len(s)):
            for i in range(index+1):
                if index-i>maxlen and s[i:index+1][0] == s[i:index+1][-1]:
                    if s[i:index+1] == s[i:index+1][::-1]:
                        longest_palindrome = s[i:index+1]
                        maxlen = index-i
        return longest_palindrome