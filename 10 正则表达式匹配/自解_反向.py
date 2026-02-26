class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        if not s:
            if p[-1] == '*':
                return self.isMatch(s, p[:-2])
            return False

        if p[-1] != '*':
            return (s[-1] == p[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1])
        else:
            return ((s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p)) or self.isMatch(s, p[:-2])
                



