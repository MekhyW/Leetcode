class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s):
            return True
        if len(s)%2:
            return False
        if s.count("(") != s.count(")") or s.count("[") != s.count("]") or s.count("{") != s.count("}"):
            return False
        pseudostack = []
        for c in s:
            if c in ['(', '[', '{']:
                pseudostack.append(c)
            elif not len(pseudostack) or (c==')' and pseudostack[-1]!='(') or (c==']' and pseudostack[-1]!='[') or (c=='}' and pseudostack[-1]!='{'):
                return False
            else:
                pseudostack.pop()
        return True