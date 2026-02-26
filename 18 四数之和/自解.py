# 特解返回也是一种剪支, 应多考虑剪支条件, 如果条件计算比较轻量, 那么其带来的优势是极大的
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        len_nums = len(nums)
        if len_nums < 4: return []

        nums.sort()
        results = []
        for cur_1 in range(len_nums - 3):
            # 跳过重复项
            if cur_1 != 0 and nums[cur_1] == nums[cur_1 - 1]:
                continue

            # 最小和剪枝 -> 加减法和判断对CPU来说成本极低, 与下面的那一堆代码相比很划算
            if nums[cur_1] + nums[cur_1 + 1] + nums[cur_1 + 2] + nums[cur_1 + 3] > target:
                break
            # 最大和剪枝
            if nums[cur_1] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
                    
            for cur_2 in range(cur_1 + 1, len_nums - 2):
                # 跳过重复项
                if cur_2 != cur_1 + 1 and nums[cur_2] == nums[cur_2 - 1]:
                    continue

                # 最小和剪枝
                if nums[cur_1] + nums[cur_2] + nums[cur_2 + 1] + nums[cur_2 + 2] > target:
                    break
                # 最大和剪枝
                if nums[cur_1] + nums[cur_2] + nums[-2] + nums[-1] < target:
                    continue

                cur_left, cur_right = cur_2 + 1, len_nums - 1
                while cur_left < cur_right:
                    sum_nums = nums[cur_1] + nums[cur_2] \
                        + nums[cur_left] + nums[cur_right] \
                        - target
                    
                    if sum_nums == 0:
                        results.append([nums[cur_1], nums[cur_2], nums[cur_left], nums[cur_right]])

                        # 只有跳过了前一位才能和前一位比较
                        cur_left += 1
                        cur_right -= 1
                        while cur_left < cur_right and nums[cur_left] == nums[cur_left - 1]:
                            cur_left += 1
                        while cur_left < cur_right and nums[cur_right] == nums[cur_right + 1]:
                            cur_right -= 1
                    elif sum_nums < 0:
                        cur_left += 1
                    else:
                        cur_right -= 1
        return results
        