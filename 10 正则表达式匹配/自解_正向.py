
def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s
    if not s:
        if len(p) >= 2 and p[1] == '*':
            return isMatch(s, p[2:])
        return False
    
    if len(p) >= 2 and p[1] == '*':
        return isMatch(s, p[2:]) or ((s[0] == p[0] or p[0] == '.') and isMatch(s[1:], p))
    else:
        return (s[0] == p[0] or p[0] == '.') and isMatch(s[1:], p[1:])
                
print(isMatch('aa', 'a*'))


