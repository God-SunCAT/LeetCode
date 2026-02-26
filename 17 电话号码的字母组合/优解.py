# hash表虽然笨, 但快
hash_n_to_c = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = [""]

        for n in digits:
            # 创建列表消耗远大于创建一个短字符串
            res = [x + y for x in res for y in hash_n_to_c[n]]

        return res