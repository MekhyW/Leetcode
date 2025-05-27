class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        balance = 0
        parts = []
        start = 0
        for i, char in enumerate(s):
            if char == '1':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                part = s[start:i+1]
                parts.append("1" + self.makeLargestSpecial(part[1:-1]) + "0")
                start = i + 1
        parts.sort(reverse=True)
        return ''.join(parts)