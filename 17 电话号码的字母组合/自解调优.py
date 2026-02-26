class Solution:
    def itos(self, digit: int):
        # 97 -> a
        if 1 < digit < 7:
            base = 97 + (digit - 2) * 3
            return [[chr(base + 0)], [chr(base + 1)], [chr(base + 2)]]
        elif digit == 7:
            return [['p'], ['q'], ['r'], ['s']]
        elif digit == 8:
            return [['t'], ['u'], ['v']]
        else:
            return [['w'], ['x'], ['y'], ['z']]

    def iter_help(self, digits, offset):
        if not offset < len(digits): return [[]]
        itos_result = self.itos(int(digits[offset]))
        branches = self.iter_help(digits, offset + 1)
        # + 是不可变加法, 这里在构建新对象, += 才是可变加法调追加
        # 字符串拼接优化:
        # CPython对 str1 += str2 和 str1 = str1 + str2 做了优化
        # 如果str1的引用计数为1, 那么其会优先在原地址扩容
        # 不管怎样, 3*3*3*... 这种做法必然会分配新内存, 那么没必要考虑考虑内存复用
        return [
            suffix + branch 
            for suffix in itos_result 
            for branch in branches
        ]

    def letterCombinations(self, digits: str) -> List[str]:
        return [''.join(chars) for chars in self.iter_help(digits, 0)]
        