class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 时间复杂度太高
        results = []
        dealt_list_a = []
        for idx1, a in enumerate(nums):
            # 若曾处理过该项, 跳过
            if a in dealt_list_a: continue

            dealt_list_c = []
            for idx2, b in enumerate(nums[idx1 + 1:]):
                # 第二项不能曾为第一项, 也不能曾为第三项
                if b in dealt_list_c or b in dealt_list_a: continue

                aim = 0 - (a + b)
                for idx3, c in enumerate(nums[idx1 + idx2 + 2:]):
                    # 第三项不能曾为第一项
                    if c in dealt_list_a: continue

                    if c == aim:
                        if not c in dealt_list_c:
                            results.append([a, b, c])
                            dealt_list_c.append(c)
                        break
            if dealt_list_c and not a in dealt_list_a:
                dealt_list_a.append(a)
        return results



            

