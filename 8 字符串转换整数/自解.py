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
        for idx, c in enumerate(s):
            if idx == 0 and (c == '+' or c == '-'): continue
            b = ord(c) - 48
            if 0 <= b <= 9:
                if p >= 214748364:
                    if p > 214748364:
                        p = 2147483647 if sign == 1 else 2147483648
                        break
                    
                    if b > 7 and sign == 1:
                        p = 2147483647
                        break
                    
                    if b > 8 and sign == -1:
                        p = 2147483648
                        break

                p = p * 10 + b
            else:
                break
        
        return p * sign

            


        
    