def longestPalindrome(s: str) -> str:
    # 格式化字符串
    s = '#' + '#'.join(s) + '#'
    s = '$' + s + '^'

    p: list[int] = []
    c, r = 0, 0
    for idx in range(len(s)):
        count = 0
        if c + r > idx:
            count = min(p[c - (idx - c)], c + r - idx)
        # 注: 当 range(a, b) 且 b <= a 时, 循环不会执行
        for i in range(count, min(idx - 0, (len(s) - 1) - idx)):
            if s[idx - (i + 1)] == s[idx + (i + 1)]:
                count += 1
            else:
                break
        if c + r < idx + count:
            c = idx
            r = count
        p.append(count)

    max_count = max(p)
    max_index = p.index(max_count)
    return s[max_index - max_count : max_index + max_count + 1].replace('#', '')
        

