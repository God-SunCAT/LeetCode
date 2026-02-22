def isPalindrome(x: int) -> bool:
    # 回文数不止可以从中间开始, 也能从两边开始
    # 正向可行, 逆向也一定可行

    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    # 取一半, 防止溢出
    reversed_number = 0
    while x > reversed_number:
        b = x % 10
        x //= 10
        reversed_number = reversed_number * 10 + b
    # 处理奇数位数, x <= reversed_number, 奇数位只可能在 reversed_number
    return x == reversed_number or x == (reversed_number // 10)

isPalindrome(1001)