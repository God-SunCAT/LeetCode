class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs): return ''
        if len(strs) == 1: return strs[0]

        len_min = 200
        for l in strs:
            len_tmp = len(l)
            # 存在空串即代表无公共前缀
            if not len_tmp: return ''

            if len_tmp < len_min:
                len_min = len_tmp
        
        count = 0
        for i in range(len_min):
            c = strs[0][i]
            for l in strs:
                if l[i] != c:
                    return l[:count]
            count += 1
        return l[:count]
