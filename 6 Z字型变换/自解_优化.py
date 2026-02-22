def convert(s: str, numRows: int) -> str:
    # 一定要考虑特殊判定, 特判是最快的
    # R - 2 < 0的情况, R > len 的情况
    if numRows == 1 or numRows >= len(s):
        return s

    p: list[str] = []
    # 解释型语言在代码层面几乎没有优化!
    n_len = len(s)
    cycle = 2 * numRows - 2
    for z in range(numRows):
        for i in range(z, n_len, cycle):
            # i -> +2 偶数项
            # i - 2*r -> -2 奇数项
            p.append(s[i])

            idx = i + cycle - 2 * z
            if 0 < z < (numRows - 1) and idx < n_len:
                p.append(s[idx])
                
    # 最后用 join 合成, 字符串加法每次都会重分配内存
    return ''.join(p)

print(convert('PAYPALISHIRING', 4))