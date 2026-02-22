def convert(s: str, numRows: int) -> str:
    p: str = ''
    for z in range(numRows):
        n = 0
        while True:
            if z == 0 or z == (numRows - 1):
                idx = numRows * n + max(numRows - 2, 0) * n + z
            elif n % 2:
                # 奇数
                # 注: 写草稿时不要对迭代对象赋值!!! 迭代对象只用于迭代!!!
                i = (n + 1) // 2
                idx = numRows * i + max(numRows - 2, 0) * i - z
            else:
                # 偶数
                i = n // 2
                idx = numRows * i + max(numRows - 2, 0) * i + z
            
            if idx >= len(s):
                break
            p += s[idx]

            n += 1
    return p

print(convert('PAYPALISHIRING', 4))