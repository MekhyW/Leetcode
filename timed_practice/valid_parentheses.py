class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s):
            return True
        if len(s)%2:
            return False
        if s.count("(") != s.count(")") or s.count("[") != s.count("]") or s.count("{") != s.count("}"):
            return False
        levels = []
        for c in s:
            if c in ['(', '[', '{']:
                levels.append(c)
            elif not len(levels) or (c==')' and levels[-1]!='(') or (c==']' and levels[-1]!='[') or (c=='}' and levels[-1]!='{'):
                return False
            else:
                levels.pop()
        return True