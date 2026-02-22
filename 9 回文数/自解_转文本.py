def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    x = str(x)

    if len(x) % 2:
        # 奇数个
        left_index = (len(x) - 1) // 2 - 1
        right_index = left_index + 2
    else:
        # 偶数数个
        left_index = len(x) // 2 - 1
        right_index = left_index + 1
    
    while left_index >= 0:
        if x[left_index] != x[right_index]:
            return False
            
        left_index -= 1
        right_index += 1
    return True

isPalindrome(121)