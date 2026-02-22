class Solution:
    def myAtoi(self, s: str) -> int:
        # 去除前导空格
        s = s.lstrip()

        # 特判
        if not len(s): return 0
        
        b = ord(s[0]) - 48
        if len(s) == 1: return b if 0 <= b <= 9 else 0

        # 符号位
        sign = -1 if s[0] == '-' else 1

        p = 0
        INT_MAX, INT_MIN = 2147483647, -2147483648
        for idx, c in enumerate(s):
            if idx == 0 and (c == '+' or c == '-'): continue
            b = ord(c) - 48
            if 0 <= b <= 9:
                if p > INT_MAX // 10 or (p == INT_MAX // 10 and b > 7): 
                    return INT_MAX if sign == 1 else INT_MIN
                    
                p = p * 10 + b
            else:
                break
        
        return p * sign

            


        
    