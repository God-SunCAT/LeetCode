def reverse(x: int) -> int:
    if not x:
        return x
    # 处理正负号
    sign = 1
    if x < 0:
        sign = -1
        x = -x

    # 计算位数
    raw = x
    count = -1
    while x:
        x //= 10
        count += 1
    
    # 反转
    p = 0
    while raw:
        b = raw % 10
        raw //= 10

        # 注意这里后面是有0占位的!
        if p >= 2147483640:
            if p > 2147483640:
                p = 0
                break
            
            if b > 7 and sign == 1:
                p = 0
                break
            
            if b > 8 and sign == -1:
                p = 0
                break

        p += b * (10 ** count)
        count -= 1

    return p * sign
