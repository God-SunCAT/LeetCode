def reverse(x: int) -> int:
    sign = 1 if x > 0 else -1
    x *= sign
    
    p = 0
    while x:
        b = x % 10
        x //= 10

        if p >= 214748364:
            if p > 214748364:
                p = 0
                break
            
            if b > 7 and sign == 1:
                p = 0
                break
            
            if b > 8 and sign == -1:
                p = 0
                break
        
        p = p * 10 + b

    return p * sign


