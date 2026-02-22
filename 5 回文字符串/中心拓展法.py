def longestPalindrome(s: str) -> str:
    # 格式化字符串
    s = '#' + '#'.join(s) + '#'
    s = '$' + s + '^'

    p: list[int] = []
    for idx in range(len(s)):
        count = 0
        # 注: for 中的 range 只用于计数, 具体计算丢给循环体
        for i in range(min(idx - 0, (len(s) - 1) - idx)):
            if s[idx - (i + 1)] == s[idx + (i + 1)]:
                count += 1
            else:
                break
        p.append(count)
    max_count = max(p)
    max_index = p.index(max_count)
    return s[max_index - max_count : max_index + max_count + 1].replace('#', '')
        

